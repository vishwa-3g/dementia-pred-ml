# Continuous associations

|                              |   mut_info |      t |    t_p |        U |    U_p |      W |    W_p |   cohen_d |   AUROC |    corr |   corr_p |
|:-----------------------------|-----------:|-------:|-------:|---------:|-------:|-------:|-------:|----------:|--------:|--------:|---------:|
| BloodOxygenLevel__Dementia.0 |    0.018   | -2.15  | 0.0324 | 2.78e+04 | 0.0326 |  2.14  | 0.032  |    0.192  |   0.555 |  0.0956 |   0.0326 |
| BloodOxygenLevel__Dementia.1 |    0.018   |  2.15  | 0.0324 | 3.47e+04 | 0.0326 | -2.14  | 0.032  |   -0.192  |   0.555 | -0.0956 |   0.0326 |
| HeartRate__Dementia.0        |    0.015   |  0.305 | 0.761  | 3.17e+04 | 0.749  | -0.32  | 0.749  |   -0.0272 |   0.508 | -0.0136 |   0.761  |
| Age__Dementia.0              |    0.0133  | -0.712 | 0.477  | 3.01e+04 | 0.472  |  0.718 | 0.472  |    0.0638 |   0.519 |  0.0319 |   0.476  |
| AlcoholLevel__Dementia.0     |    0.00019 | -0.99  | 0.323  | 2.96e+04 | 0.319  |  0.997 | 0.319  |    0.0886 |   0.526 |  0.0443 |   0.323  |
| AlcoholLevel__Dementia.1     |    0.00019 |  0.99  | 0.323  | 3.28e+04 | 0.319  | -0.997 | 0.319  |   -0.0886 |   0.526 | -0.0443 |   0.323  |
| HeartRate__Dementia.1        |    0       | -0.305 | 0.761  | 3.07e+04 | 0.749  |  0.32  | 0.749  |    0.0272 |   0.508 |  0.0136 |   0.761  |
| BodyTemperature__Dementia.0  |    0       |  1.81  | 0.0704 | 3.41e+04 | 0.0777 | -1.77  | 0.0772 |   -0.162  |   0.546 | -0.0809 |   0.0708 |
| BodyTemperature__Dementia.1  |    0       | -1.81  | 0.0704 | 2.84e+04 | 0.0777 |  1.77  | 0.0772 |    0.162  |   0.546 |  0.0809 |   0.0708 |
| Weight__Dementia.0           |    0       | -1.04  | 0.299  | 2.95e+04 | 0.288  |  1.06  | 0.29   |    0.0933 |   0.528 |  0.0467 |   0.297  |
| Weight__Dementia.1           |    0       |  1.04  | 0.299  | 3.29e+04 | 0.288  | -1.06  | 0.29   |   -0.0933 |   0.528 | -0.0467 |   0.297  |
| Age__Dementia.1              |    0       |  0.712 | 0.477  | 3.24e+04 | 0.472  | -0.718 | 0.472  |   -0.0638 |   0.519 | -0.0319 |   0.476  |

# Categorical associations

|                                       |   mut_info |   cramer_v |       H |      H_p |
|:--------------------------------------|-----------:|-----------:|--------:|---------:|
| Depression_Status                     |   0.233    |          0 |   0     | 0        |
| Depression_Status__Dementia.0         |   0.233    |          0 |  70.2   | 0        |
| Depression_Status__Dementia.1         |   0.233    |          0 |  56.6   | 0        |
| APOE_ε4                               |   0.0923   |          0 |   0     | 0        |
| APOE_ε4__Dementia.1                   |   0.0923   |          0 |  41.2   | 1.39e-10 |
| APOE_ε4__Dementia.0                   |   0.0923   |          0 |  30.8   | 2.88e-08 |
| Smoking_Status__Dementia.1            |   0.0719   |          0 | 355     | 0        |
| Smoking_Status__Dementia.0            |   0.0719   |          0 | 340     | 0        |
| Smoking_Status                        |   0.0719   |          0 |   0     | 0        |
| Education_Level                       |   0.0194   |          0 |   0     | 0        |
| Education_Level__Dementia.0           |   0.0194   |          0 | 379     | 0        |
| Education_Level__Dementia.1           |   0.0194   |          0 | 389     | 0        |
| Chronic_Health_Conditions             |   0.00347  |          0 |   0     | 0        |
| Chronic_Health_Conditions__Dementia.0 |   0.00347  |          0 |  23     | 1.58e-06 |
| Chronic_Health_Conditions__Dementia.1 |   0.00347  |          0 |  28.8   | 7.96e-08 |
| Family_History                        |   0.00198  |          0 |   0     | 0        |
| Family_History__Dementia.0            |   0.00198  |          0 |   0.064 | 0.8      |
| Family_History__Dementia.1            |   0.00198  |          0 |   1.29  | 0.255    |
| Gender__Dementia.0                    |   0.00142  |          0 |   1.15  | 0.283    |
| Gender__Dementia.1                    |   0.00142  |          0 |   0.036 | 0.85     |
| Gender                                |   0.00142  |          0 |   0     | 0        |
| Physical_Activity__Dementia.0         |   0.00105  |          0 |  77.7   | 0        |
| Physical_Activity                     |   0.00105  |          0 |   0     | 0        |
| Physical_Activity__Dementia.1         |   0.00105  |          0 |  88.2   | 0        |
| Nutrition_Diet__Dementia.0            |   0.000629 |          0 | 104     | 0        |
| Nutrition_Diet__Dementia.1            |   0.000629 |          0 | 115     | 0        |
| Nutrition_Diet                        |   0.000629 |          0 |   0     | 0        |
| Domi   t_Hand                         |   0.000167 |          0 |   0     | 0        |
| Domi   t_Hand__Dementia.1             |   0.000167 |          0 |   2.11  | 0.146    |
| Domi   t_Hand__Dementia.0             |   0.000167 |          0 |   0.324 | 0.569    |
| Diabetic__Dementia.0                  |   0.00013  |          0 |   0.144 | 0.704    |
| Diabetic__Dementia.1                  |   0.00013  |          0 |   0.256 | 0.613    |
| Diabetic                              |   0.00013  |          0 |   0     | 0        |
| Sleep_Quality__Dementia.0             |   4.49e-05 |          0 |   0.144 | 0.704    |
| Sleep_Quality__Dementia.1             |   4.49e-05 |          0 |   1.6   | 0.206    |
| Sleep_Quality                         |   4.49e-05 |          0 |   0     | 0        |
| Medication_History                    |   6.28e-09 |          0 |   0     | 0        |
| Medication_History__Dementia.1        |   6.28e-09 |          0 |   0.256 | 0.613    |
| Medication_History__Dementia.0        |   6.28e-09 |          0 |   0.144 | 0.704    |

**Note**: values less than 1e-10 are rounded to zero.
