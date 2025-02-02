############   CITATION    ##########

#->https://www.geeksforgeeks.org/use-pandas-to-calculate-stats-from-an-imported-csv-file/


import pandas as pd


df = pd.read_csv('/Users/gagandeepsingh/Documents/MLD/dementia_patients_health_data.csv')
df_male = pd.read_csv('/Users/gagandeepsingh/Documents/MLD/df-analyze/male.csv')
df_female = pd.read_csv('/Users/gagandeepsingh/Documents/MLD/df-analyze/female.csv')

#Main Dataset
df_D_0 = pd.read_csv('./Dementia_0_D.csv')
df_D_1 = pd.read_csv('./Dementia_1_D.csv')

#Male dataset
df_M_0 = pd.read_csv('/Users/gagandeepsingh/Documents/MLD/df-analyze/Dementia_0_Male.csv')
df_M_1 = pd.read_csv('/Users/gagandeepsingh/Documents/MLD/df-analyze/Dementia_1_Male.csv')


# Female Dataset
df_F_0 = pd.read_csv('./Dementia_0_Female.csv')
df_F_1 = pd.read_csv('./Dementia_1_Female.csv')

#Dropping unneccesry column
df = df.drop(['MRI_Delay'],axis=1)

columns_to_drop = ['Prescription','Dosage in mg']

male_df = df[df['Gender'] == 'Male']
female_df = df[df['Gender'] == 'Female']

# Filtered data to new CSV files
male_df.to_csv("male.csv", index=False)
female_df.to_csv("female.csv", index=False)

# print("Dataset created")

#For Dementia.csv
dementia_0_D = df[df['Dementia'] == 0]
dementia_1_D = df[df['Dementia'] == 1]

dementia_0_D = dementia_0_D.drop(columns_to_drop,axis=1)
dementia_0_D.to_csv("Dementia_0_D.csv",index=False)
dementia_1_D.to_csv("Dementia_1_D.csv",index=False)


#Male.csv
dementia_0_M = df_male[df_male['Dementia'] == 0]
dementia_1_M = df_male[df_male['Dementia'] == 1]

dementia_0_M = dementia_0_M.drop(columns_to_drop,axis=1)
dementia_0_M.to_csv("Dementia_0_Male.csv",index=False)
dementia_1_M.to_csv("Dementia_1_Male.csv",index=False)


#For Female
dementia_0_F = df_female[df_female['Dementia'] == 0]
dementia_1_F = df_female[df_female['Dementia'] == 1]

dementia_0_F = dementia_0_F.drop(columns_to_drop,axis=1)
dementia_0_F.to_csv("Dementia_0_Female.csv",index=False)
dementia_1_F.to_csv("Dementia_1_Female.csv",index=False)


# Command to show the mean and standard deviation of the columns
print("\n-----------Results(Mean,Std. Deviation)-> Dementia_patients_health_data.csv-----------")
print("\n-------------For Dementia_0_D.csv------------------")

#####  CODE ISCITED ABOVE   ####### 

for col in df_D_0 .columns:
    if pd.api.types.is_numeric_dtype(df_D_0[col]):  
        m_val = df_D_0[col].mean()
        st_d = df_D_0[col].std()
        print(f'{col}')
        print(f'Mean: {m_val}')
        print(f'Standard Deviation: {st_d}\n')


print("\n------------For Dementia_1_D------------------------")

for col in df_D_1.columns:
    if pd.api.types.is_numeric_dtype(df_D_1[col]):  
        m_val = df_D_1[col].mean()
        st_d = df_D_1[col].std()
        print(f' {col}')
        print(f'Mean: {m_val}')
        print(f'Standard Deviation: {st_d}\n')


print("\n-----------Results(Mean,Std. Deviation)-> Dementia_Male.csv-----------")
print("\n-------------For Dementia_0_Male.csv------------------")
for col in df_M_0.columns:
    if pd.api.types.is_numeric_dtype(df_M_0[col]):  
        m_val = df_M_0[col].mean()
        st_d = df_M_0[col].std()
        print(f' {col}')
        print(f'Mean: {m_val}')
        print(f'Standard Deviation: {st_d}\n')



print("\n------------For Dementia_1_Male------------------------")

for col in df_M_1.columns:
    if pd.api.types.is_numeric_dtype(df_M_1[col]):  
        m_val = df_M_1[col].mean()
        st_d = df_M_1[col].std()
        print(f' {col}')
        print(f'Mean: {m_val}')
        print(f'Standard Deviation: {st_d}\n')




print("\n-----------Results(Mean,Std. Deviation)-> Dementia_Female.csv-----------")
print("\n-------------For Dementia_0_Female.csv------------------")

for col in df_F_0.columns:
    if pd.api.types.is_numeric_dtype(df_F_0[col]):  
        m_val = df_F_0[col].mean()
        st_dev = df_F_0[col].std()
        print(f' {col}')
        print(f'Mean: {m_val}')
        print(f'Standard Deviation: {st_d}\n')



# print("\n------------For Dementia_1_Female------------------------")

for col in df_F_1.columns:
    if pd.api.types.is_numeric_dtype(df_F_1[col]):  
        m_val = df_F_1[col].mean()
        st_dev = df_F_1[col].std()
        print(f' {col}')
        print(f'Mean: {m_val}')
        print(f'Standard Deviation: {st_dev}\n')


