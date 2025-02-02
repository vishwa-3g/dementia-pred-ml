# Wrapper-Based Feature Selection Summary

Wrapper method:    StepUp
Wrapper model:     Linear
Redundancy-aware:  True

## Selected Features

['Depression_Status_Yes', 'Diabetic_1', 'BodyTemperature', 'Age']

## Selection Scores (Accuracy: Higher = More important)

| feature               |     score |
|:----------------------|----------:|
| Depression_Status_Yes | 7.855e-01 |
| Diabetic_1            | 7.855e-01 |
| BodyTemperature       | 5.512e-01 |
| Age                   | 5.159e-01 |

# Redundant Stepwise Selection Results

Metric: Accuracy

* Depression_Status_Yes (Accuracy=0.78549) - [Iteration   0]
* Diabetic_1 (Accuracy=0.78549) - [Iteration   1]

redundants                                 score
---------------------------------------  -------
Diabetic_1                                0.7855
Sleep_Quality_Poor                        0.7855
Chronic_Health_Conditions_Diabetes        0.7855
Chronic_Health_Conditions_Heart Disease   0.7855
APOE_ε4_Positive                          0.7855
Nutrition_Diet_Low-Carb Diet              0.7855
Smoking_Status_Current Smoker             0.7855
Education_Level_No School                 0.7855
Smoking_Status_Former Smoker              0.7855
Physical_Activity_Moderate Activity       0.7855
Education_Level_Diploma/Degree            0.7855
Education_Level_Secondary School          0.7855
AlcoholLevel                              0.7855
Nutrition_Diet_Balanced Diet              0.7855
Dominant_Hand_Right                       0.7855
Medication_History_Yes                    0.7855
Physical_Activity_Sedentary               0.7855
Chronic_Health_Conditions_nan             0.7855
Family_History_Yes                        0.7855
Nutrition_Diet_Mediterranean Diet         0.7855
Education_Level_Primary School            0.7855
Smoking_Status_Never Smoked               0.7855
Chronic_Health_Conditions_Hypertension    0.7855
Physical_Activity_Mild Activity           0.7855

* BodyTemperature (Accuracy=0.55122) - [Iteration   2]
* Age (Accuracy=0.51592) - [Iteration   3]

redundants          score
----------------  -------
Age                0.5159
HeartRate          0.5159
BloodOxygenLevel   0.5159
Weight             0.5159

