# from faker import Faker

# # Playing around with faker stuff
# fake = Faker('nl_NL')

# Faker.seed(18)
# for _ in range(10):
#     print(fake.company())   # so, this shit is really, really bad. Unusable

import pandas as pd

# Uploaded cleaned company names (wikipedia) and generated pseudonames using website (http://www.lexique.org/shiny/unipseudo/)
# Open and merge lexique generated pseudonames 
pseudonames = pd.Series(dtype=object)
for number in range(3, 12):
    with open('./stimuli_creation/data/raw/pilot/generated_pseudo_company_names_length' + str(number) +'.xlsx', 'rb') as f:
        temp_series = pd.read_excel(f)
        pseudonames = pd.concat([pseudonames, temp_series])

company_names = pseudonames.Pseudoword.rename('name').reset_index(drop=True)

# company_names = company_names.sample(400, random_state = 1)
# print(company_names.to_string())

company_names_pilot = company_names.sample(20 , random_state = 1)

company_names_pilot.to_csv('./stimuli_creation/data/cleaned/pilot/company_names_pilot.csv', encoding='utf-8', index=False)