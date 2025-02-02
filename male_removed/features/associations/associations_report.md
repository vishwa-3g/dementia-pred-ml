# Continuous associations

|                              |   mut_info |      t |     t_p |        U |     U_p |      W |     W_p |   cohen_d |   AUROC |    corr |   corr_p |
|:-----------------------------|-----------:|-------:|--------:|---------:|--------:|-------:|--------:|----------:|--------:|--------:|---------:|
| BodyTemperature__Dementia.0  |    0.0643  |  3.09  | 0.00222 | 9.34e+03 | 0.00319 | -3.01  | 0.00264 |   -0.392  |   0.608 | -0.193  |  0.00226 |
| BodyTemperature__Dementia.1  |    0.0643  | -3.09  | 0.00222 | 6.02e+03 | 0.00319 |  3.01  | 0.00264 |    0.392  |   0.608 |  0.193  |  0.00226 |
| HeartRate__Dementia.0        |    0.0147  |  0.861 | 0.39    | 8.15e+03 | 0.404   | -0.834 | 0.404   |   -0.109  |   0.531 | -0.0547 |  0.391   |
| HeartRate__Dementia.1        |    0.0145  | -0.861 | 0.39    | 7.21e+03 | 0.404   |  0.834 | 0.404   |    0.109  |   0.531 |  0.0547 |  0.391   |
| Age__Dementia.1              |    0.00712 |  1.02  | 0.31    | 8.24e+03 | 0.318   | -0.996 | 0.319   |   -0.13   |   0.537 | -0.0648 |  0.309   |
| Age__Dementia.0              |    0.0042  | -1.02  | 0.31    | 7.12e+03 | 0.318   |  0.996 | 0.319   |    0.13   |   0.537 |  0.0648 |  0.309   |
| AlcoholLevel__Dementia.0     |    0       | -0.595 | 0.552   | 7.36e+03 | 0.573   |  0.563 | 0.573   |    0.0757 |   0.521 |  0.0379 |  0.552   |
| AlcoholLevel__Dementia.1     |    0       |  0.595 | 0.552   | 8e+03    | 0.573   | -0.563 | 0.573   |   -0.0757 |   0.521 | -0.0379 |  0.552   |
| BloodOxygenLevel__Dementia.0 |    0       | -1.71  | 0.0889  | 6.7e+03  | 0.0824  |  1.75  | 0.0809  |    0.217  |   0.564 |  0.108  |  0.0895  |
| BloodOxygenLevel__Dementia.1 |    0       |  1.71  | 0.0889  | 8.66e+03 | 0.0824  | -1.75  | 0.0809  |   -0.217  |   0.564 | -0.108  |  0.0895  |
| Weight__Dementia.0           |    0       | -0.699 | 0.485   | 7.26e+03 | 0.459   |  0.736 | 0.462   |    0.0891 |   0.527 |  0.0447 |  0.484   |
| Weight__Dementia.1           |    0       |  0.699 | 0.485   | 8.1e+03  | 0.459   | -0.736 | 0.462   |   -0.0891 |   0.527 | -0.0447 |  0.484   |

# Categorical associations

|                                       |   mut_info |   cramer_v |         H |      H_p |
|:--------------------------------------|-----------:|-----------:|----------:|---------:|
| Depression_Status__Dementia.1         |   0.209    |          0 |  33.6     | 6.72e-09 |
| Depression_Status                     |   0.209    |          0 |   0       | 0        |
| Depression_Status__Dementia.0         |   0.209    |          0 |  42.1     | 0        |
| Smoking_Status                        |   0.091    |          0 |   0       | 0        |
| Smoking_Status__Dementia.1            |   0.091    |          0 | 154       | 0        |
| Smoking_Status__Dementia.0            |   0.091    |          0 | 146       | 0        |
| APOE_ε4__Dementia.1                   |   0.0626   |          0 |  22.5     | 2.13e-06 |
| APOE_ε4__Dementia.0                   |   0.0626   |          0 |  16.3     | 5.41e-05 |
| APOE_ε4                               |   0.0626   |          0 |   0       | 0        |
| Education_Level                       |   0.0111   |          0 |   0       | 0        |
| Education_Level__Dementia.0           |   0.0111   |          0 | 215       | 0        |
| Education_Level__Dementia.1           |   0.0111   |          0 | 221       | 0        |
| Physical_Activity__Dementia.0         |   0.00706  |          0 |  45.4     | 0        |
| Physical_Activity                     |   0.00706  |          0 |   0       | 0        |
| Physical_Activity__Dementia.1         |   0.00706  |          0 |  51.7     | 0        |
| Sleep_Quality__Dementia.0             |   0.00208  |          0 |   0.129   | 0.72     |
| Sleep_Quality__Dementia.1             |   0.00208  |          0 |   0.129   | 0.72     |
| Sleep_Quality                         |   0.00208  |          0 |   0       | 0        |
| Nutrition_Diet__Dementia.0            |   0.000374 |          0 |  46.8     | 0        |
| Nutrition_Diet__Dementia.1            |   0.000374 |          0 |  53.1     | 0        |
| Nutrition_Diet                        |   0.000374 |          0 |   0       | 0        |
| Medication_History__Dementia.0        |   0.000275 |          0 |   0.394   | 0.53     |
| Medication_History                    |   0.000275 |          0 |   0       | 0        |
| Medication_History__Dementia.1        |   0.000275 |          0 |   0.00805 | 0.928    |
| Domi   t_Hand                         |   0.000263 |          0 |   0       | 0        |
| Domi   t_Hand__Dementia.1             |   0.000263 |          0 |   0.652   | 0.419    |
| Domi   t_Hand__Dementia.0             |   0.000263 |          0 |   0.00806 | 0.928    |
| Chronic_Health_Conditions__Dementia.0 |   0.000119 |          0 |  12.3     | 0.000455 |
| Chronic_Health_Conditions             |   0.000119 |          0 |   0       | 0        |
| Chronic_Health_Conditions__Dementia.1 |   0.000119 |          0 |  15.6     | 7.68e-05 |
| Diabetic__Dementia.0                  |   3.47e-05 |          0 |   0.0725  | 0.788    |
| Diabetic                              |   3.47e-05 |          0 |   0       | 0        |
| Diabetic__Dementia.1                  |   3.47e-05 |          0 |   0.201   | 0.654    |
| Family_History                        |   3.41e-06 |          0 |   0       | 0        |
| Family_History__Dementia.1            |   3.41e-06 |          0 |   1.58    | 0.209    |
| Family_History__Dementia.0            |   3.41e-06 |          0 |   0.291   | 0.59     |

**Note**: values less than 1e-10 are rounded to zero.
