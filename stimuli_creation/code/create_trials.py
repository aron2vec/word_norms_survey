import pandas as pd

## Trials without associations have been created using bestworst_tools. These files 
## have been excluded from the GitHub due to license and redistribution ambiguity.
## However, for information: random trials have been generated for our 200 seed words 
## in such a way that every trial is unique and that any two words do not appear 
## together in any trial more than once.

## PILOT
# We have to add both a wordtype column and an association column to the DFs for PsychoPy to correctly function.
company_names_pilot = pd.read_csv("./stimuli_creation/data/trials/pilot/company_bestworst_pilot_trials.xlsx")
nonwords_pilot = pd.read_csv("./stimuli_creation/data/trials/pilot/nonwords_bestworst_pilot_trials.xlsx")
dutch_names_pilot = pd.read_csv("./stimuli_creation/data/trials/pilot/dutch_bestworst_pilot_trials.xlsx")

company_names_pilot['wordtype'] = 'namen'
nonwords_pilot['wordtype'] = 'woorden'
dutch_names_pilot['wordtype'] = 'namen'

company_names_pilot['association'] = 'kwaadaardigheid'
company_names_pilot['association'][int(len(company_names_pilot)/2):] = 'vrouwelijkheid'
company_names_pilot = company_names_pilot.sample(frac=1)

nonwords_pilot['association'] = 'kwaadaardigheid'
nonwords_pilot['association'][int(len(nonwords_pilot)/2):] = 'vrouwelijkheid'
nonwords_pilot = nonwords_pilot.sample(frac=1)

dutch_names_pilot['association'] = 'kwaadaardigheid'
dutch_names_pilot['association'][int(len(dutch_names_pilot)/2):] = 'vrouwelijkheid'
dutch_names_pilot = dutch_names_pilot.sample(frac=1)

company_names_pilot.to_excel("./stimuli_creation/data/trials/pilot/company_bestworst_pilot_trials.xlsx", index=False)
nonwords_pilot.to_excel("./stimuli_creation/data/trials/pilot/nonwords_bestworst_pilot_trials.xlsx", index=False)
dutch_names_pilot.to_excel("./stimuli_creation/data/trials/pilot/dutch_bestworst_pilot_trials.xlsx", index=False)

## Final Survey

company_names = pd.read_csv("./stimuli_creation/data/trials/final_survey/company_bestworst_final_trials.csv")
nonwords = pd.read_csv("./stimuli_creation/data/trials/final_survey/nonwords_bestworst_final_trials.csv")
dutch_names = pd.read_csv("./stimuli_creation/data/trials/final_survey/dutch_bestworst_final_trials.csv")

def association_inserter_and_integrator(name, df, trials_per_participant):
    concat_df = pd.DataFrame(columns = ['option1', 'option2', 'option3', 'option4', 'association'])

    n_assoc = [1, 2, 3, 4]
    assoc_list = ['vrouwelijk', 'slecht', 'betrouwbaar', 'slim']
    for number, association in zip(n_assoc, assoc_list):
        globals()[name+'_assoc%s' % number] = df.copy()
        globals()[name+'_assoc%s' % number].insert(len(df.columns), 'association', association)
        globals()[name+'_assoc%s' % number] = globals()[name+'_assoc%s' % number].sample(frac=1, random_state=number).reset_index(drop=True)

    for i in range(0, len(df)):
        concat_df = pd.concat([concat_df, 
                                globals()[name+'_assoc1'].iloc[[i]], 
                                globals()[name+'_assoc2'].iloc[[i]], 
                                globals()[name+'_assoc3'].iloc[[i]], 
                                globals()[name+'_assoc4'].iloc[[i]]])
        
    output_df = pd.DataFrame(columns = ['option1', 'option2', 'option3', 'option4', 'association'])

    for i in range(0, 100):
        lower = int(i * (trials_per_participant/3))
        upper = int(((i+1) * (trials_per_participant/3)))

        output_df = pd.concat([output_df, concat_df.iloc[lower:upper].sample(frac=1, random_state=i)])
          
    output_df = output_df.reset_index(drop=True)

    return output_df


company_names_final = association_inserter_and_integrator('company_names', company_names, 192)
nonwords_final = association_inserter_and_integrator('nonwords', nonwords, 192)
dutch_names_final = association_inserter_and_integrator('dutch_names', dutch_names, 192)

company_names_final['wordtype'] = 'bedrijfsnamen'
nonwords_final['wordtype'] = 'nepwoorden'
dutch_names_final['wordtype'] = 'namen'

company_names_final.to_excel("./stimuli_creation/data/trials/final_survey/company_bestworst_final_trials.xlsx", index=False)
nonwords_final.to_excel("./stimuli_creation/data/trials/final_survey/nonwords_bestworst_final_trials.xlsx", index=False)
dutch_names_final.to_excel("./stimuli_creation/data/trials/final_survey/dutch_bestworst_final_trials.xlsx", index=False)