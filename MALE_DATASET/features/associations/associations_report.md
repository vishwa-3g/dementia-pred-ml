# Continuous associations

|                                   |   mut_info |       t |    t_p |        U |    U_p |        W |    W_p |   cohen_d |   AUROC |     corr |   corr_p |
|:----------------------------------|-----------:|--------:|-------:|---------:|-------:|---------:|-------:|----------:|--------:|---------:|---------:|
| Cognitive_Test_Scores__Dementia.0 |     0.694  | -27     | 0      | 0        | 0      |  inf     | 0      |    3.21   |   1     |  0.85    |   0      |
| Cognitive_Test_Scores__Dementia.1 |     0.694  |  27     | 0      | 2.2e+04  | 0      | -inf     | 0      |   -3.21   |   1     | -0.85    |   0      |
| Dosage_in_mg__Dementia.0          |     0.582  |   2.35  | 0.02   | 1.06e+04 | 0.499  |    0.513 | 0.608  |   -0.282  |   0.521 | -0.14    |   0.0159 |
| Dosage_in_mg__Dementia.1          |     0.571  |  -2.35  | 0.02   | 1.15e+04 | 0.499  |   -0.513 | 0.608  |    0.282  |   0.521 |  0.14    |   0.0159 |
| BloodOxygenLevel__Dementia.0      |     0.0553 |  -2.33  | 0.0202 | 9.26e+03 | 0.0174 |    2.4   | 0.0164 |    0.27   |   0.58  |  0.134   |   0.0207 |
| BloodOxygenLevel__Dementia.1      |     0.0553 |   2.33  | 0.0202 | 1.28e+04 | 0.0174 |   -2.4   | 0.0164 |   -0.27   |   0.58  | -0.134   |   0.0207 |
| BodyTemperature__Dementia.0       |     0.0447 |   1.99  | 0.0472 | 1.24e+04 | 0.054  |   -1.93  | 0.0531 |   -0.231  |   0.565 | -0.115   |   0.0473 |
| BodyTemperature__Dementia.1       |     0.0447 |  -1.99  | 0.0472 | 9.59e+03 | 0.054  |    1.93  | 0.0531 |    0.231  |   0.565 |  0.115   |   0.0473 |
| HeartRate__Dementia.0             |     0.0267 |   0.123 | 0.902  | 1.11e+04 | 0.898  |   -0.128 | 0.898  |   -0.0143 |   0.504 | -0.00718 |   0.902  |
| Weight__Dementia.0                |     0.0255 |  -1.32  | 0.189  | 1e+04    | 0.18   |    1.34  | 0.18   |    0.153  |   0.545 |  0.0767  |   0.188  |
| Weight__Dementia.1                |     0.0255 |   1.32  | 0.189  | 1.2e+04  | 0.18   |   -1.34  | 0.18   |   -0.153  |   0.545 | -0.0767  |   0.188  |
| HeartRate__Dementia.1             |     0.0165 |  -0.123 | 0.902  | 1.09e+04 | 0.898  |    0.128 | 0.898  |    0.0143 |   0.504 |  0.00718 |   0.902  |
| AlcoholLevel__Dementia.0          |     0      |   0.762 | 0.447  | 1.15e+04 | 0.491  |   -0.689 | 0.491  |   -0.0885 |   0.523 | -0.0443  |   0.447  |
| AlcoholLevel__Dementia.1          |     0      |  -0.762 | 0.447  | 1.05e+04 | 0.491  |    0.689 | 0.491  |    0.0885 |   0.523 |  0.0443  |   0.447  |
| Age__Dementia.0                   |     0      |  -0.983 | 0.326  | 1.03e+04 | 0.304  |    1.02  | 0.308  |    0.115  |   0.534 |  0.0574  |   0.325  |
| Age__Dementia.1                   |     0      |   0.983 | 0.326  | 1.18e+04 | 0.304  |   -1.02  | 0.308  |   -0.115  |   0.534 | -0.0574  |   0.325  |

# Categorical associations

|                                       |   mut_info |   cramer_v |        H |      H_p |
|:--------------------------------------|-----------:|-----------:|---------:|---------:|
| Prescription                          |   0.693    |    1       |   0      | 0        |
| Prescription__Dementia.0              |   0.693    |    1       | 284      | 0        |
| Prescription__Dementia.1              |   0.693    |    1       | 289      | 0        |
| Depression_Status                     |   0.218    |    0.583   |   0      | 0        |
| Depression_Status__Dementia.1         |   0.218    |    0.583   |  37.7    | 8.46e-10 |
| Depression_Status__Dementia.0         |   0.218    |    0.583   |  46.9    | 0        |
| APOE_ε4                               |   0.0709   |    0.367   |   0      | 0        |
| APOE_ε4__Dementia.0                   |   0.0709   |    0.367   |  19.7    | 8.85e-06 |
| APOE_ε4__Dementia.1                   |   0.0709   |    0.367   |  26.7    | 2.39e-07 |
| Smoking_Status__Dementia.0            |   0.0646   |    0.307   | 210      | 0        |
| Smoking_Status__Dementia.1            |   0.0646   |    0.307   | 219      | 0        |
| Smoking_Status                        |   0.0646   |    0.307   |   0      | 0        |
| Education_Level__Dementia.0           |   0.017    |    0.182   | 260      | 0        |
| Education_Level                       |   0.017    |    0.182   |   0      | 0        |
| Education_Level__Dementia.1           |   0.017    |    0.182   | 266      | 0        |
| Family_History__Dementia.0            |   0.00532  |    0.103   |   0.0606 | 0.806    |
| Family_History                        |   0.00532  |    0.103   |   0      | 0        |
| Family_History__Dementia.1            |   0.00532  |    0.103   |   0.968  | 0.325    |
| Physical_Activity                     |   0.00322  |    0.0802  |   0      | 0        |
| Physical_Activity__Dementia.1         |   0.00322  |    0.0802  |  59      | 0        |
| Physical_Activity__Dementia.0         |   0.00322  |    0.0802  |  52      | 0        |
| Chronic_Health_Conditions             |   0.00139  |    0.0527  |   0      | 0        |
| Chronic_Health_Conditions__Dementia.1 |   0.00139  |    0.0527  |  10.1    | 0.0015   |
| Chronic_Health_Conditions__Dementia.0 |   0.00139  |    0.0527  |   7.19   | 0.00731  |
| Nutrition_Diet__Dementia.0            |   0.00126  |    0.0501  |  55.2    | 0        |
| Nutrition_Diet__Dementia.1            |   0.00126  |    0.0501  |  62.2    | 0        |
| Nutrition_Diet                        |   0.00126  |    0.0501  |   0      | 0        |
| Domi   t_Hand                         |   0.00117  |    0.0483  |   0      | 0        |
| Domi   t_Hand__Dementia.1             |   0.00117  |    0.0483  |   0.33   | 0.565    |
| Domi   t_Hand__Dementia.0             |   0.00117  |    0.0483  |   1.72   | 0.189    |
| Sleep_Quality__Dementia.0             |   0.00092  |    0.0429  |   0      | 1        |
| Sleep_Quality__Dementia.1             |   0.00092  |    0.0429  |   0.545  | 0.461    |
| Sleep_Quality                         |   0.00092  |    0.0429  |   0      | 0        |
| Diabetic__Dementia.0                  |   0.000523 |    0.0323  |   0.168  | 0.682    |
| Diabetic__Dementia.1                  |   0.000523 |    0.0323  |   1.32   | 0.251    |
| Diabetic                              |   0.000523 |    0.0323  |   0      | 0        |
| Medication_History                    |   3.03e-05 |    0.00778 |   0      | 0        |
| Medication_History__Dementia.1        |   3.03e-05 |    0.00778 |   0.33   | 0.565    |
| Medication_History__Dementia.0        |   3.03e-05 |    0.00778 |   1.72   | 0.189    |

**Note**: values less than 1e-10 are rounded to zero.
