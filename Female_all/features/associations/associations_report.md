# Continuous associations

|                                   |   mut_info |        t |    t_p |        U |   U_p |        W |   W_p |   cohen_d |   AUROC |     corr |   corr_p |
|:----------------------------------|-----------:|---------:|-------:|---------:|------:|---------:|------:|----------:|--------:|---------:|---------:|
| Cognitive_Test_Scores__Dementia.0 |     0.695  | -23.8    | 0      | 0        | 0     |  inf     | 0     |   3.07    |   1     |  0.839   |   0      |
| Cognitive_Test_Scores__Dementia.1 |     0.695  |  23.8    | 0      | 1.59e+04 | 0     | -inf     | 0     |  -3.07    |   1     | -0.839   |   0      |
| Dosage_in_mg__Dementia.0          |     0.569  |   2.39   | 0.0183 | 8.32e+03 | 0.459 |   -0.565 | 0.572 |  -0.311   |   0.525 | -0.154   |   0.0142 |
| Dosage_in_mg__Dementia.1          |     0.55   |  -2.39   | 0.0183 | 7.54e+03 | 0.459 |    0.565 | 0.572 |   0.311   |   0.525 |  0.154   |   0.0142 |
| BloodOxygenLevel__Dementia.0      |     0.0116 |  -0.816  | 0.415  | 7.53e+03 | 0.485 |    0.696 | 0.486 |   0.103   |   0.525 |  0.0515  |   0.415  |
| BloodOxygenLevel__Dementia.1      |     0.0116 |   0.816  | 0.415  | 8.33e+03 | 0.485 |   -0.696 | 0.486 |  -0.103   |   0.525 | -0.0515  |   0.415  |
| AlcoholLevel__Dementia.0          |     0      |  -0.411  | 0.681  | 7.7e+03  | 0.695 |    0.392 | 0.695 |   0.0519  |   0.514 |  0.026   |   0.681  |
| AlcoholLevel__Dementia.1          |     0      |   0.411  | 0.681  | 8.16e+03 | 0.695 |   -0.392 | 0.695 |  -0.0519  |   0.514 | -0.026   |   0.681  |
| HeartRate__Dementia.0             |     0      |  -0.532  | 0.595  | 7.63e+03 | 0.601 |    0.523 | 0.601 |   0.067   |   0.519 |  0.0336  |   0.596  |
| HeartRate__Dementia.1             |     0      |   0.532  | 0.595  | 8.23e+03 | 0.601 |   -0.523 | 0.601 |  -0.067   |   0.519 | -0.0336  |   0.596  |
| BodyTemperature__Dementia.0       |     0      |  -0.4    | 0.689  | 7.69e+03 | 0.681 |    0.411 | 0.681 |   0.0504  |   0.515 |  0.0253  |   0.69   |
| BodyTemperature__Dementia.1       |     0      |   0.4    | 0.689  | 8.17e+03 | 0.681 |   -0.411 | 0.681 |  -0.0504  |   0.515 | -0.0253  |   0.69   |
| Weight__Dementia.0                |     0      |  -0.706  | 0.481  | 7.53e+03 | 0.487 |    0.689 | 0.491 |   0.0893  |   0.525 |  0.0447  |   0.479  |
| Weight__Dementia.1                |     0      |   0.706  | 0.481  | 8.33e+03 | 0.487 |   -0.689 | 0.491 |  -0.0893  |   0.525 | -0.0447  |   0.479  |
| Age__Dementia.0                   |     0      |  -0.0765 | 0.939  | 7.85e+03 | 0.894 |    0.134 | 0.894 |   0.00963 |   0.505 |  0.00483 |   0.939  |
| Age__Dementia.1                   |     0      |   0.0765 | 0.939  | 8.01e+03 | 0.894 |   -0.134 | 0.894 |  -0.00963 |   0.505 | -0.00483 |   0.939  |

# Categorical associations

|                                       |   mut_info |   cramer_v |        H |      H_p |
|:--------------------------------------|-----------:|-----------:|---------:|---------:|
| Prescription                          |   0.693    |          0 |   0      | 0        |
| Prescription__Dementia.1              |   0.693    |          0 | 228      | 0        |
| Prescription__Dementia.0              |   0.693    |          0 | 223      | 0        |
| Depression_Status__Dementia.0         |   0.251    |          0 |  31.9    | 1.61e-08 |
| Depression_Status__Dementia.1         |   0.251    |          0 |  24.6    | 7.11e-07 |
| Depression_Status                     |   0.251    |          0 |   0      | 0        |
| APOE_ε4__Dementia.0                   |   0.135    |          0 |  13.8    | 0.000199 |
| APOE_ε4__Dementia.1                   |   0.135    |          0 |  19.5    | 9.88e-06 |
| APOE_ε4                               |   0.135    |          0 |   0      | 0        |
| Smoking_Status__Dementia.1            |   0.059    |          0 | 205      | 0        |
| Smoking_Status__Dementia.0            |   0.059    |          0 | 197      | 0        |
| Smoking_Status                        |   0.059    |          0 |   0      | 0        |
| Education_Level__Dementia.0           |   0.0241   |          0 | 164      | 0        |
| Education_Level__Dementia.1           |   0.0241   |          0 | 170      | 0        |
| Education_Level                       |   0.0241   |          0 |   0      | 0        |
| Chronic_Health_Conditions__Dementia.0 |   0.0119   |          0 |  11.5    | 0.000697 |
| Chronic_Health_Conditions__Dementia.1 |   0.0119   |          0 |  14.9    | 0.000116 |
| Chronic_Health_Conditions             |   0.0119   |          0 |   0      | 0        |
| Family_History__Dementia.1            |   0.00816  |          0 |   0.0317 | 0.859    |
| Family_History__Dementia.0            |   0.00816  |          0 |   0.285  | 0.593    |
| Family_History                        |   0.00816  |          0 |   0      | 0        |
| Nutrition_Diet__Dementia.0            |   0.00539  |          0 |  55.5    | 0        |
| Nutrition_Diet                        |   0.00539  |          0 |   0      | 0        |
| Nutrition_Diet__Dementia.1            |   0.00539  |          0 |  62.1    | 0        |
| Domi   t_Hand__Dementia.1             |   0.00145  |          0 |   0.959  | 0.328    |
| Domi   t_Hand                         |   0.00145  |          0 |   0      | 0        |
| Domi   t_Hand__Dementia.0             |   0.00145  |          0 |   0.0714 | 0.789    |
| Physical_Activity__Dementia.0         |   0.00116  |          0 |  36.6    | 1.43e-09 |
| Physical_Activity__Dementia.1         |   0.00116  |          0 |  42.4    | 0        |
| Physical_Activity                     |   0.00116  |          0 |   0      | 0        |
| Sleep_Quality__Dementia.0             |   0.000886 |          0 |   0.199  | 0.656    |
| Sleep_Quality__Dementia.1             |   0.000886 |          0 |   1.34   | 0.247    |
| Sleep_Quality                         |   0.000886 |          0 |   0      | 0        |
| Medication_History                    |   0.000103 |          0 |   0      | 0        |
| Medication_History__Dementia.1        |   0.000103 |          0 |   0.792  | 0.373    |
| Medication_History__Dementia.0        |   0.000103 |          0 |   0.0317 | 0.859    |
| Diabetic__Dementia.1                  |   2.96e-05 |          0 |   0.0713 | 0.789    |
| Diabetic__Dementia.0                  |   2.96e-05 |          0 |   0.198  | 0.656    |
| Diabetic                              |   2.96e-05 |          0 |   0      | 0        |

**Note**: values less than 1e-10 are rounded to zero.
