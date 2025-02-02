import pandas as pd

df = pd.read_csv("/Users/gagandeepsingh/Documents/MLD/df-analyze/dementia_patients_health_data.csv")

columns_to_drop = ['Prescription','Dosage in mg','Cognitive_Test_Scores']
W_Pres = df.drop(["Prescription", "Dosage in mg"],axis = 1)

W_Pres.to_csv("Dementia_wp_Pres.csv",index = False)

w_pres_cogn = df.drop(columns_to_drop,axis = 1)

W_Cogn = df.drop(['Cognitive_Test_Scores'],axis = 1)
W_Cogn.to_csv("Dementia_w_Cogn.csv",index = False)

w_pres_cogn.to_csv("W_Pres_Cogn.csv",index = False)


#Converting the dataset to Male and female
male_df = df[df['Gender'] == 'Male']
female_df = df[df['Gender'] == 'Female']

#Creating new male and femel dataset
male_df.to_csv("male.csv", index=False)
female_df.to_csv("female.csv", index=False)


#Read datasets For male and female
df_male = pd.read_csv('/Users/gagandeepsingh/Documents/MLD/df-analyze/male.csv')
df_female = pd.read_csv('/Users/gagandeepsingh/Documents/MLD/df-analyze/female.csv')

df_male = df_male.drop(columns_to_drop,axis=1)
df_female = df_female.drop(columns_to_drop,axis=1)

df_male.to_csv("Male_drop.csv",index=False)
df_female.to_csv("Female_drop.csv",index=False)




# python3 df-analyze.py --spreadsheet <path of the dementia file> -target Dementia --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --feat-select filter embed wrap --redudant-wrapper-selection --embed-select lgbm linear -wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --test-val-size 0.4 --outdir ./results         