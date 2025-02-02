# Wrapper-Based Feature Selection Summary

Wrapper method:    StepUp
Wrapper model:     Linear
Redundancy-aware:  True

## Selected Features

['Depression_Status_Yes', 'Education_Level_Primary School', 'Weight', 'BodyTemperature', 'Age', 'HeartRate', 'BloodOxygenLevel']

## Selection Scores (Accuracy: Higher = More important)

| feature                        |     score |
|:-------------------------------|----------:|
| Depression_Status_Yes          | 7.500e-01 |
| Education_Level_Primary School | 7.500e-01 |
| Weight                         | 5.242e-01 |
| BodyTemperature                | 5.322e-01 |
| Age                            | 5.524e-01 |
| HeartRate                      | 5.443e-01 |
| BloodOxygenLevel               | 5.042e-01 |

# Redundant Stepwise Selection Results

Metric: Accuracy

* Depression_Status_Yes (Accuracy=0.74996) - [Iteration   0]
* Education_Level_Primary School (Accuracy=0.74996) - [Iteration   1]

redundants                                 score
---------------------------------------  -------
Education_Level_Primary School            0.7500
Chronic_Health_Conditions_Diabetes        0.7500
Chronic_Health_Conditions_Heart Disease   0.7500
Physical_Activity_Moderate Activity       0.7500
Physical_Activity_Sedentary               0.7500
Chronic_Health_Conditions_Hypertension    0.7500
Smoking_Status_Never Smoked               0.7500
Nutrition_Diet_Balanced Diet              0.7500
Smoking_Status_Former Smoker              0.7500
Education_Level_Diploma/Degree            0.7500
Smoking_Status_Current Smoker             0.7500
Education_Level_No School                 0.7500
APOE_ε4_Positive                          0.7500
Sleep_Quality_Poor                        0.7500
Education_Level_Secondary School          0.7500
Physical_Activity_Mild Activity           0.7500
Nutrition_Diet_Mediterranean Diet         0.7500
Diabetic_1                                0.7500
Chronic_Health_Conditions_nan             0.7500
Nutrition_Diet_Low-Carb Diet              0.7500
AlcoholLevel                              0.7500
Family_History_Yes                        0.7500
Dominant_Hand_Right                       0.7500
Medication_History_Yes                    0.7500

* Weight (Accuracy=0.52424) - [Iteration   2]
* BodyTemperature (Accuracy=0.53224) - [Iteration   3]
* Age (Accuracy=0.55241) - [Iteration   4]
* HeartRate (Accuracy=0.54433) - [Iteration   5]
* BloodOxygenLevel (Accuracy=0.50416) - [Iteration   6]
