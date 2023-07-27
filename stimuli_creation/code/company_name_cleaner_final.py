import pandas as pd
import nltk
import pickle


# Data import & choose only the column with company names
company_names = pd.read_excel("./stimuli_creation/data/raw/final_survey/Export 13_03_2023 15_52.xlsx", sheet_name='Results')
company_names = company_names['Company name Latin alphabet'].rename('company_name')

# Find frequent 4- and 5-grams and delete word parts that contain these (excluding spaces, but I would say including punctuation)
ngrams_4 = pd.Series(dtype=object)
ngrams_5 = pd.Series(dtype=object)
for name in company_names.items():
    ngrams_4 = pd.concat([ngrams_4, pd.Series(nltk.ngrams(name[1], 4))])
    ngrams_5 = pd.concat([ngrams_5, pd.Series(nltk.ngrams(name[1], 5))])

ngrams_4 = ngrams_4.reset_index(drop = True)
ngrams_5 = ngrams_5.reset_index(drop = True)

# Save for potential later use
with open('./stimuli_creation/data/pickle/ngrams_4.pickle', 'wb') as f:
    pickle.dump(ngrams_4, f)
with open('./stimuli_creation/data/pickle/ngrams_5.pickle', 'wb') as f:
    pickle.dump(ngrams_5, f)
    
# Do some extra cleaning, so the rows contain strings instead of tuples + they don't include ngrams that contain a space
ngrams_4 = pd.Series([str().join(tup) for tup in ngrams_4])
ngrams_4 = ngrams_4.drop(ngrams_4[ngrams_4.str.contains(' ')].index)

ngrams_5 = pd.Series([str().join(tup) for tup in ngrams_5])
ngrams_5 = ngrams_5.drop(ngrams_5[ngrams_5.str.contains(' ')].index)

# Choose the ngrams that we will use for deleting unnecessary company name information
# (for 5grams, all values with occurrence count >400, for 4grams only B.V.)
flagged_ngrams = pd.concat([ngrams_4.value_counts()[:1], ngrams_5.value_counts()[ngrams_5.value_counts().values > 400]]).index.to_list()

# Clean the company names list
company_names_cleaned = []

for name in company_names:
    # for every name in the list
    cleaned_name = []
    for subname in name.split():
        # split into subnames
        if any(flagged_ngram in subname for flagged_ngram in flagged_ngrams) == True:
            # check if the subname contains any illegal ngrams, if so, don't save
            continue
        else:
            # if no illegal subnames, remove punctuation and numbers
            subname = subname.translate(str.maketrans('', '', '!"#$%&\'()*+,-/.:;<=>?@[\\]^_`{|}~1234567890')).strip()
            if subname:
                # if the subname is not empty after punctuation removal, add it to the list of legal subnames
                cleaned_name.append(subname) 
    # add all legal subnames together, with a space in between   
    cleaned_name = " ".join(cleaned_name)
    if cleaned_name:
        # if the string is not empty, lowercast and append to the full list of cleaned names
        company_names_cleaned.append(cleaned_name.lower())
    else:
        continue

# Save as txt
with open('./stimuli_creation/data/raw/final_survey/company_names_final_survey_precleaned.txt', 'w') as f:
    for name in company_names_cleaned:
        f.write(name+'\n')

# Uploaded cleaned company names and generated pseudonames using website (http://www.lexique.org/shiny/unipseudo/)
# Open and merge lexique generated pseudonames 
pseudonames = pd.Series(dtype=object)
for number in range(5, 16):
    with open('./stimuli_creation/data/raw/final_survey/generated_pseudo_company_names_final_survey_len' + str(number) +'.xlsx', 'rb') as f:
        temp_series = pd.read_excel(f)
        pseudonames = pd.concat([pseudonames, temp_series])

pseudonames = pseudonames.Pseudoword.reset_index(drop=True)
pseudonames = pseudonames.drop(pseudonames[pseudonames.str.contains(' ')].index).reset_index(drop=True)
pseudonames = pseudonames.str.capitalize()

# Choose 200 random names, save to csv
company_names_final = pseudonames.sample(200 , random_state=1)
company_names_final.to_csv('./stimuli_creation/data/cleaned/final_survey/company_names_final.csv', index=False)