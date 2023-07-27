# data source: http://crr.ugent.be/archives/1796

import pandas as pd
import statistics

## IMPORT DATA
nonwords = pd.read_csv('./stimuli_creation/data/raw/final_survey/The_Dutch_Lexicon_Project_2.csv', encoding = 'utf_8', sep = ';')

## Data Cleaning
# Remove lexical words and illegal characters
nonwords = nonwords[nonwords.lexicality == 'N']
nonwords = nonwords.drop(nonwords[nonwords.spelling.str.contains('Ö|ö|ø|ô|ó|è|É|é|á|ã|â|å|ä|Ü|ü|ú|ĝ|ğ|ı|İ|ł|Ç|ç|Ş|ş|š|Š| |\'|-', regex=True) == True].index)

# remove all unnecessary columns, and rename the one left over
nonwords = nonwords.spelling.rename('nonword')

# Sample 400 nonwords, tweak random state to ensure all words are actually nonwords 
nonwords_stimuli = nonwords.sample(400, random_state=18).sort_values()


# Show some information about the final stimulus nonwords, and compare it to the overall nonword dataset
# print(nonwords_stimuli_final.to_string())
# print('Character length total sample; max: {}, min: {}, mean: {}'.format(max(nonwords.map(len)), min(nonwords.map(len)), statistics.mean(nonwords.map(len))))

## FOR THE PILOT TEST (get only 20 words)
nonwords_pilot = nonwords_stimuli.sample(20 , random_state = 1)
nonwords_pilot.to_csv('./stimuli_creation/data/cleaned/pilot/nonwords_pilot.csv', encoding='utf-8', index=False)

## We ended up changing the number of words to 200, since the sampled nonwords for the pilot tests were also derived from the already picked 400, 
## instead of sampling 200 new ones, I will just subsample 200 from the initial 400 as well.
nonwords_stimuli = nonwords_stimuli.sample(200, random_state = 1)

nonwords_stimuli.to_csv('./stimuli_creation/data/cleaned/final_survey/nonwords_final.csv', encoding='utf-8', index=False)
