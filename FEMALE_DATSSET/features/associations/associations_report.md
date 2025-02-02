# Continuous associations

|                                   |   mut_info |       t |    t_p |        U |   U_p |        W |   W_p |   cohen_d |   AUROC |    corr |   corr_p |
|:----------------------------------|-----------:|--------:|-------:|---------:|------:|---------:|------:|----------:|--------:|--------:|---------:|
| Cognitive_Test_Scores__Dementia.0 |   0.694    | -24.2   | 0      | 0        | 0     |  inf     | 0     |    2.86   |   1     |  0.82   |   0      |
| Cognitive_Test_Scores__Dementia.1 |   0.694    |  24.2   | 0      | 2.28e+04 | 0     | -inf     | 0     |   -2.86   |   1     | -0.82   |   0      |
| Dosage_in_mg__Dementia.1          |   0.491    |  -2.46  | 0.0149 | 1.18e+04 | 0.567 |   -0.442 | 0.658 |    0.293  |   0.517 |  0.145  |   0.0114 |
| Dosage_in_mg__Dementia.0          |   0.472    |   2.46  | 0.0149 | 1.1e+04  | 0.567 |    0.442 | 0.658 |   -0.293  |   0.517 | -0.145  |   0.0114 |
| HeartRate__Dementia.0             |   0.0124   |  -1.27  | 0.204  | 1.04e+04 | 0.19  |    1.31  | 0.189 |    0.147  |   0.544 |  0.0733 |   0.204  |
| Age__Dementia.0                   |   0.00537  |  -0.418 | 0.676  | 1.11e+04 | 0.664 |    0.435 | 0.664 |    0.0482 |   0.514 |  0.0241 |   0.676  |
| HeartRate__Dementia.1             |   0.00407  |   1.27  | 0.204  | 1.24e+04 | 0.19  |   -1.31  | 0.189 |   -0.147  |   0.544 | -0.0733 |   0.204  |
| Weight__Dementia.0                |   0.00126  |  -1.54  | 0.124  | 1.02e+04 | 0.133 |    1.5   | 0.133 |    0.178  |   0.55  |  0.0887 |   0.124  |
| Weight__Dementia.1                |   0.00126  |   1.54  | 0.124  | 1.25e+04 | 0.133 |   -1.5   | 0.133 |   -0.178  |   0.55  | -0.0887 |   0.124  |
| BloodOxygenLevel__Dementia.0      |   0.000644 |  -1.1   | 0.273  | 1.05e+04 | 0.254 |    1.14  | 0.255 |    0.126  |   0.538 |  0.0632 |   0.274  |
| BloodOxygenLevel__Dementia.1      |   0.000644 |   1.1   | 0.273  | 1.23e+04 | 0.254 |   -1.14  | 0.255 |   -0.126  |   0.538 | -0.0632 |   0.274  |
| AlcoholLevel__Dementia.0          |   0        |   0.52  | 0.603  | 1.17e+04 | 0.668 |   -0.427 | 0.669 |   -0.06   |   0.514 | -0.0301 |   0.603  |
| AlcoholLevel__Dementia.1          |   0        |  -0.52  | 0.603  | 1.11e+04 | 0.668 |    0.427 | 0.669 |    0.06   |   0.514 |  0.0301 |   0.603  |
| BodyTemperature__Dementia.0       |   0        |  -1.42  | 0.157  | 1.03e+04 | 0.145 |    1.47  | 0.143 |    0.163  |   0.549 |  0.0815 |   0.158  |
| BodyTemperature__Dementia.1       |   0        |   1.42  | 0.157  | 1.25e+04 | 0.145 |   -1.47  | 0.143 |   -0.163  |   0.549 | -0.0815 |   0.158  |
| Age__Dementia.1                   |   0        |   0.418 | 0.676  | 1.17e+04 | 0.664 |   -0.435 | 0.664 |   -0.0482 |   0.514 | -0.0241 |   0.676  |

# Categorical associations

|                                       |   mut_info |   cramer_v |        H |      H_p |
|:--------------------------------------|-----------:|-----------:|---------:|---------:|
| Prescription__Dementia.0              |   0.693    |     1      | 276      | 0        |
| Prescription__Dementia.1              |   0.693    |     1      | 282      | 0        |
| Prescription                          |   0.693    |     1      |   0      | 0        |
| Depression_Status__Dementia.1         |   0.233    |     0.605  |  33.8    | 6.14e-09 |
| Depression_Status__Dementia.0         |   0.233    |     0.605  |  43.5    | 0        |
| Depression_Status                     |   0.233    |     0.605  |   0      | 0        |
| APOE_ε4__Dementia.0                   |   0.13     |     0.489  |  13.8    | 0.000198 |
| APOE_ε4__Dementia.1                   |   0.13     |     0.489  |  20.5    | 6.11e-06 |
| APOE_ε4                               |   0.13     |     0.489  |   0      | 0        |
| Smoking_Status__Dementia.0            |   0.0537   |     0.279  | 221      | 0        |
| Smoking_Status                        |   0.0537   |     0.279  |   0      | 0        |
| Smoking_Status__Dementia.1            |   0.0537   |     0.279  | 231      | 0        |
| Education_Level__Dementia.0           |   0.0266   |     0.228  | 202      | 0        |
| Education_Level__Dementia.1           |   0.0266   |     0.228  | 209      | 0        |
| Education_Level                       |   0.0266   |     0.228  |   0      | 0        |
| Chronic_Health_Conditions             |   0.00963  |     0.138  |   0      | 0        |
| Chronic_Health_Conditions__Dementia.1 |   0.00963  |     0.138  |  15.1    | 0.0001   |
| Chronic_Health_Conditions__Dementia.0 |   0.00963  |     0.138  |  11.3    | 0.000783 |
| Physical_Activity__Dementia.1         |   0.0046   |     0.0958 |  46.2    | 0        |
| Physical_Activity                     |   0.0046   |     0.0958 |   0      | 0        |
| Physical_Activity__Dementia.0         |   0.0046   |     0.0958 |  39.4    | 3.44e-10 |
| Family_History__Dementia.0            |   0.00177  |     0.0594 |   0.106  | 0.745    |
| Family_History__Dementia.1            |   0.00177  |     0.0594 |   0.238  | 0.626    |
| Family_History                        |   0.00177  |     0.0594 |   0      | 0        |
| Domi   t_Hand                         |   0.000926 |     0.043  |   0      | 0        |
| Domi   t_Hand__Dementia.0             |   0.000926 |     0.043  |   2.39   | 0.122    |
| Domi   t_Hand__Dementia.1             |   0.000926 |     0.043  |   0.538  | 0.463    |
| Nutrition_Diet                        |   0.000296 |     0.0243 |   0      | 0        |
| Nutrition_Diet__Dementia.1            |   0.000296 |     0.0243 |  53.3    | 0        |
| Nutrition_Diet__Dementia.0            |   0.000296 |     0.0243 |  45.9    | 0        |
| Medication_History__Dementia.0        |   0.000287 |     0.0239 |   0.325  | 0.569    |
| Medication_History__Dementia.1        |   0.000287 |     0.0239 |   1.91   | 0.167    |
| Medication_History                    |   0.000287 |     0.0239 |   0      | 0        |
| Sleep_Quality__Dementia.0             |   0.00026  |     0.0228 |   0.425  | 0.515    |
| Sleep_Quality__Dementia.1             |   0.00026  |     0.0228 |   2.14   | 0.143    |
| Sleep_Quality                         |   0.00026  |     0.0228 |   0      | 0        |
| Diabetic__Dementia.0                  |   0.000211 |     0.0205 |   0.0265 | 0.871    |
| Diabetic__Dementia.1                  |   0.000211 |     0.0205 |   0.423  | 0.515    |
| Diabetic                              |   0.000211 |     0.0205 |   0      | 0        |

**Note**: values less than 1e-10 are rounded to zero.
