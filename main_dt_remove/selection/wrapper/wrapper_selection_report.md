# Wrapper-Based Feature Selection Summary

Wrapper method:    StepUp
Wrapper model:     Linear
Redundancy-aware:  True

## Selected Features

['Depression_Status_Yes', 'Gender_Male', 'BodyTemperature', 'Weight', 'Age', 'HeartRate', 'BloodOxygenLevel']

## Selection Scores (Accuracy: Higher = More important)

| feature               |     score |
|:----------------------|----------:|
| Depression_Status_Yes | 7.700e-01 |
| Gender_Male           | 7.700e-01 |
| BodyTemperature       | 7.540e-01 |
| Weight                | 6.060e-01 |
| Age                   | 6.000e-01 |
| HeartRate             | 5.740e-01 |
| BloodOxygenLevel      | 6.000e-01 |

# Redundant Stepwise Selection Results

Metric: Accuracy

* Depression_Status_Yes (Accuracy=0.77000) - [Iteration   0]
* Gender_Male (Accuracy=0.77000) - [Iteration   1]

redundants                                 score
---------------------------------------  -------
Gender_Male                               0.7700
Education_Level_Diploma/Degree            0.7700
Education_Level_Secondary School          0.7700
Chronic_Health_Conditions_Heart Disease   0.7700
Chronic_Health_Conditions_nan             0.7700
Diabetic_1                                0.7700
Nutrition_Diet_Mediterranean Diet         0.7700
Sleep_Quality_Poor                        0.7700
Chronic_Health_Conditions_Diabetes        0.7700
Dominant_Hand_Right                       0.7700
Smoking_Status_Current Smoker             0.7700
Education_Level_No School                 0.7700
Smoking_Status_Never Smoked               0.7700
APOE_ε4_Positive                          0.7700
Chronic_Health_Conditions_Hypertension    0.7700
Physical_Activity_Mild Activity           0.7700
AlcoholLevel                              0.7700
Nutrition_Diet_Balanced Diet              0.7700
Physical_Activity_Moderate Activity       0.7700
Smoking_Status_Former Smoker              0.7700
Education_Level_Primary School            0.7700
Family_History_Yes                        0.7700
Physical_Activity_Sedentary               0.7700
Nutrition_Diet_Low-Carb Diet              0.7700
Medication_History_Yes                    0.7700

* BodyTemperature (Accuracy=0.75400) - [Iteration   2]
* Weight (Accuracy=0.60600) - [Iteration   3]
* Age (Accuracy=0.60000) - [Iteration   4]
* HeartRate (Accuracy=0.57400) - [Iteration   5]
* BloodOxygenLevel (Accuracy=0.60000) - [Iteration   6]
