# -*- coding: utf-8 -*-
# data source: http://www.naamkunde.net/?page_id=293

import pandas as pd
import statistics
import random
import math

## IMPORT DATA
dutch_names = pd.read_csv('./stimuli_creation/data/raw/final_survey/top_10000_babynamen.txt', encoding = 'utf_8', sep = '\t')

## Data Cleaning
# drop names with space in them
dutch_names = dutch_names.drop(dutch_names[dutch_names.Naam.str.split(' ').map(len) != 2].index)

# split first column to name and gender, add a total frequency count column, delete the others, rename columns
dutch_names[['name', 'gender']] = dutch_names['Naam'].str.split(' ', expand = True)

# drop unnecessary columns
dutch_names = dutch_names.drop(columns=['Naam', '1985-1989', '1990-1994', '1995-1999', '2000-2004'])

# rename column with total frequencies to 
dutch_names = dutch_names.rename(columns={'1983-2006' : 'total_freq'})
dutch_names = dutch_names[['name', 'gender', 'total_freq']]

# change gender to binary (0 = female, 1 = male)
dutch_names.gender[dutch_names.gender == '(V)'] = 0
dutch_names.gender[dutch_names.gender == '(M)'] = 1

# delete names with illegal characters & single-charactered names
dutch_names = dutch_names.drop(dutch_names[dutch_names.name.map(len) < 2].index)
dutch_names = dutch_names.drop(dutch_names[dutch_names.name.str.contains('Ö|ö|ø|ô|ó|è|É|é|á|ã|â|å|ä|Ü|ü|ú|ĝ|ğ|ı|İ|ł|Ç|ç|Ş|ş|š|Š| |\'|-', regex=True) == True].index)

# delete bottom 25% of names
dutch_names = dutch_names.drop(dutch_names[dutch_names.total_freq <= 40].index)

# create two dataframes, one for male & for female, sorted on frequency (high to low)
dutch_names_female = dutch_names[dutch_names.gender == 0].sort_values(['total_freq', 'name'], ascending = [False, True])
dutch_names_male = dutch_names[dutch_names.gender == 1].sort_values(['total_freq', 'name'], ascending = [False, True])

# randomly sample 200 male and 200 female names, in slices of 5 (tweaking the seed to get 400 unique names)
dutch_names_combined = pd.DataFrame([], columns=['name', 'gender'])

for dataframe in [dutch_names_female, dutch_names_male]:
    slice_length = math.ceil(len(dataframe)/5)
    for slice in range(0, len(dataframe), slice_length):
        dutch_names_combined = pd.concat([dutch_names_combined, dataframe[['name', 'gender']].iloc[slice : slice + slice_length].sample(40, random_state=38)])

## FOR THE PILOT TEST (get only 20 names)
dutch_names_pilot = dutch_names_combined.sample(20 , random_state=1)
dutch_names_pilot.to_csv('./stimuli_creation/data/cleaned/pilot/dutch_names_pilot.csv', encoding='utf-8', index=False)

## FOR FINAL SURVEY (derive 200 names)
# We ended up changing the number of words to 200, since the sampled names for the pilot tests were also derived from the already picked 400, 
# instead of sampling 200 new ones, I will just subsample 200 from the initial 400 as well.
dutch_names_final = dutch_names_combined.groupby('gender', group_keys=False).apply(lambda x: x.sample(100, random_state=2))
dutch_names_final = dutch_names_final.name.sort_values()

dutch_names_final.to_csv('./stimuli_creation/data/cleaned/final_survey/dutch_names_final.csv', encoding='utf-8', index=False)

