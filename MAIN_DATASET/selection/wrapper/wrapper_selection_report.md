# Wrapper-Based Feature Selection Summary

Wrapper method:    StepUp
Wrapper model:     Linear
Redundancy-aware:  True

## Selected Features

['Prescription_nan', 'HeartRate']

## Selection Scores (Accuracy: Higher = More important)

| feature          |     score |
|:-----------------|----------:|
| Prescription_nan | 1.000e+00 |
| HeartRate        | 1.000e+00 |

# Redundant Stepwise Selection Results

Metric: Accuracy

* Prescription_nan (Accuracy=1.00000) - [Iteration   0]

redundants          score
----------------  -------
Prescription_nan   1.0000
Dosage_in_mg_NAN   1.0000

* HeartRate (Accuracy=1.00000) - [Iteration   1]

redundants                                 score
---------------------------------------  -------
HeartRate                                 1.0000
Family_History_Yes                        1.0000
Physical_Activity_Moderate Activity       1.0000
Physical_Activity_nan                     1.0000
Depression_Status_nan                     1.0000
Family_History_nan                        1.0000
Education_Level_Primary School            1.0000
Prescription_Memantine                    1.0000
Smoking_Status_nan                        1.0000
Smoking_Status_Current Smoker             1.0000
Nutrition_Diet_Low-Carb Diet              1.0000
Chronic_Health_Conditions_Diabetes        1.0000
Diabetic_1.0                              1.0000
Smoking_Status_Former Smoker              1.0000
Chronic_Health_Conditions_nan             1.0000
Physical_Activity_Mild Activity           1.0000
Gender_nan                                1.0000
Prescription_Donepezil                    1.0000
Sleep_Quality_nan                         1.0000
Education_Level_nan                       1.0000
Dosage_in_mg                              1.0000
Prescription_Galantamine                  1.0000
Diabetic_nan                              1.0000
Education_Level_No School                 1.0000
Nutrition_Diet_Mediterranean Diet         1.0000
Dominant_Hand_Right                       1.0000
Cognitive_Test_Scores                     1.0000
Medication_History_Yes                    1.0000
AlcoholLevel                              1.0000
Nutrition_Diet_Balanced Diet              1.0000
APOE_ε4_nan                               1.0000
Prescription_Rivastigmine                 1.0000
Gender_Male                               1.0000
Weight                                    1.0000
Depression_Status_Yes                     1.0000
Sleep_Quality_Poor                        1.0000
Medication_History_nan                    1.0000
Dominant_Hand_nan                         1.0000
Education_Level_Secondary School          1.0000
BodyTemperature                           1.0000
APOE_ε4_Positive                          1.0000
Chronic_Health_Conditions_Hypertension    1.0000
Nutrition_Diet_nan                        1.0000
Chronic_Health_Conditions_Heart Disease   1.0000
Smoking_Status_Never Smoked               1.0000
BloodOxygenLevel                          1.0000
Age                                       1.0000
Education_Level_Diploma/Degree            1.0000
Physical_Activity_Sedentary               1.0000

