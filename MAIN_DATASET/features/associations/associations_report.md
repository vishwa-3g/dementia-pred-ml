# Continuous associations

|                                   |   mut_info |       t |      t_p |        U |    U_p |        W |    W_p |   cohen_d |   AUROC |    corr |   corr_p |
|:----------------------------------|-----------:|--------:|---------:|---------:|-------:|---------:|-------:|----------:|--------:|--------:|---------:|
| Cognitive_Test_Scores__Dementia.0 |    0.694   | -36.6   | 0        | 0        | 0      |  inf     | 0      |    3.06   |   1     |  0.838  | 0        |
| Cognitive_Test_Scores__Dementia.1 |    0.694   |  36.6   | 0        | 8.99e+04 | 0      | -inf     | 0      |   -3.06   |   1     | -0.838  | 0        |
| Dosage_in_mg__Dementia.0          |    0.588   |   3.37  | 0.000867 | 4.34e+04 | 0.427  |    0.603 | 0.546  |   -0.283  |   0.517 | -0.14   | 0.000562 |
| Dosage_in_mg__Dementia.1          |    0.581   |  -3.37  | 0.000867 | 4.65e+04 | 0.427  |   -0.603 | 0.546  |    0.283  |   0.517 |  0.14   | 0.000562 |
| Age__Dementia.1                   |    0.0281  |   0.865 | 0.387    | 4.69e+04 | 0.361  |   -0.907 | 0.364  |   -0.0709 |   0.522 | -0.0355 | 0.386    |
| BloodOxygenLevel__Dementia.0      |    0.0208  |  -2.39  | 0.0173   | 4e+04    | 0.0197 |    2.34  | 0.0193 |    0.195  |   0.555 |  0.0972 | 0.0173   |
| BloodOxygenLevel__Dementia.1      |    0.0208  |   2.39  | 0.0173   | 4.99e+04 | 0.0197 |   -2.34  | 0.0193 |   -0.195  |   0.555 | -0.0972 | 0.0173   |
| Weight__Dementia.0                |    0.00492 |  -1.79  | 0.0735   | 4.12e+04 | 0.0762 |    1.77  | 0.076  |    0.147  |   0.542 |  0.0732 | 0.073    |
| Weight__Dementia.1                |    0.00492 |   1.79  | 0.0735   | 4.87e+04 | 0.0762 |   -1.77  | 0.076  |   -0.147  |   0.542 | -0.0732 | 0.073    |
| AlcoholLevel__Dementia.0          |    0       |   0.754 | 0.451    | 4.64e+04 | 0.483  |   -0.699 | 0.485  |   -0.0617 |   0.517 | -0.0309 | 0.45     |
| AlcoholLevel__Dementia.1          |    0       |  -0.754 | 0.451    | 4.35e+04 | 0.483  |    0.699 | 0.485  |    0.0617 |   0.517 |  0.0309 | 0.45     |
| HeartRate__Dementia.0             |    0       |  -0.336 | 0.737    | 4.42e+04 | 0.707  |    0.376 | 0.707  |    0.0275 |   0.509 |  0.0138 | 0.737    |
| HeartRate__Dementia.1             |    0       |   0.336 | 0.737    | 4.58e+04 | 0.707  |   -0.376 | 0.707  |   -0.0275 |   0.509 | -0.0138 | 0.737    |
| BodyTemperature__Dementia.0       |    0       |  -0.612 | 0.541    | 4.33e+04 | 0.448  |    0.757 | 0.449  |    0.0499 |   0.518 |  0.025  | 0.542    |
| BodyTemperature__Dementia.1       |    0       |   0.612 | 0.541    | 4.66e+04 | 0.448  |   -0.757 | 0.449  |   -0.0499 |   0.518 | -0.025  | 0.542    |
| Age__Dementia.0                   |    0       |  -0.865 | 0.387    | 4.3e+04  | 0.361  |    0.907 | 0.364  |    0.0709 |   0.522 |  0.0355 | 0.386    |

# Categorical associations

|                                       |   mut_info |   cramer_v |        H |      H_p |
|:--------------------------------------|-----------:|-----------:|---------:|---------:|
| Prescription__Dementia.0              |   0.693    |    1       | 566      | 0        |
| Prescription__Dementia.1              |   0.693    |    1       | 577      | 0        |
| Prescription                          |   0.693    |    1       |   0      | 0        |
| Depression_Status__Dementia.1         |   0.24     |    0.613   |  63.9    | 0        |
| Depression_Status__Dementia.0         |   0.24     |    0.613   |  81      | 0        |
| Depression_Status                     |   0.24     |    0.613   |   0      | 0        |
| APOE_ε4__Dementia.0                   |   0.0889   |    0.408   |  41.4    | 1.22e-10 |
| APOE_ε4                               |   0.0889   |    0.408   |   0      | 0        |
| APOE_ε4__Dementia.1                   |   0.0889   |    0.408   |  55.6    | 0        |
| Smoking_Status__Dementia.1            |   0.0614   |    0.299   | 442      | 0        |
| Smoking_Status__Dementia.0            |   0.0614   |    0.299   | 424      | 0        |
| Smoking_Status                        |   0.0614   |    0.299   |   0      | 0        |
| Education_Level                       |   0.0205   |    0.201   |   0      | 0        |
| Education_Level__Dementia.0           |   0.0205   |    0.201   | 417      | 0        |
| Education_Level__Dementia.1           |   0.0205   |    0.201   | 430      | 0        |
| Family_History                        |   0.00419  |    0.0915  |   0      | 0        |
| Family_History__Dementia.1            |   0.00419  |    0.0915  |   3      | 0.0833   |
| Family_History__Dementia.0            |   0.00419  |    0.0915  |   0.481  | 0.488    |
| Chronic_Health_Conditions             |   0.00376  |    0.0863  |   0      | 0        |
| Chronic_Health_Conditions__Dementia.1 |   0.00376  |    0.0863  |  23.5    | 1.24e-06 |
| Chronic_Health_Conditions__Dementia.0 |   0.00376  |    0.0863  |  17.2    | 3.28e-05 |
| Nutrition_Diet                        |   0.00127  |    0.0503  |   0      | 0        |
| Nutrition_Diet__Dementia.1            |   0.00127  |    0.0503  | 111      | 0        |
| Nutrition_Diet__Dementia.0            |   0.00127  |    0.0503  |  97.5    | 0        |
| Medication_History__Dementia.1        |   0.000594 |    0.0345  |   1.33   | 0.248    |
| Medication_History                    |   0.000594 |    0.0345  |   0      | 0        |
| Medication_History__Dementia.0        |   0.000594 |    0.0345  |   0.0133 | 0.908    |
| Diabetic__Dementia.0                  |   0.000488 |    0.0312  |   0.03   | 0.862    |
| Diabetic__Dementia.1                  |   0.000488 |    0.0312  |   1.47   | 0.226    |
| Diabetic                              |   0.000488 |    0.0312  |   0      | 0        |
| Physical_Activity__Dementia.0         |   0.000397 |    0.0282  |  94.7    | 0        |
| Physical_Activity                     |   0.000397 |    0.0282  |   0      | 0        |
| Physical_Activity__Dementia.1         |   0.000397 |    0.0282  | 108      | 0        |
| Sleep_Quality__Dementia.1             |   6.29e-05 |    0.0112  |   1.47   | 0.226    |
| Sleep_Quality__Dementia.0             |   6.29e-05 |    0.0112  |   0.03   | 0.862    |
| Sleep_Quality                         |   6.29e-05 |    0.0112  |   0      | 0        |
| Domi   t_Hand                         |   5.41e-05 |    0.0104  |   0      | 0        |
| Domi   t_Hand__Dementia.1             |   5.41e-05 |    0.0104  |   0.0833 | 0.773    |
| Domi   t_Hand__Dementia.0             |   5.41e-05 |    0.0104  |   0.563  | 0.453    |
| Gender                                |   4.42e-05 |    0.00941 |   0      | 0        |
| Gender__Dementia.1                    |   4.42e-05 |    0.00941 |   0.03   | 0.863    |
| Gender__Dementia.0                    |   4.42e-05 |    0.00941 |   0.749  | 0.387    |

**Note**: values less than 1e-10 are rounded to zero.
