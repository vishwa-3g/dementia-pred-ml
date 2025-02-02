# Continuous predictions

| feature               | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:----------------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| Cognitive_Test_Scores | sgd-linear | 1      |  1      | 1      | 1      | 1      |    1      |
| Dosage_in_mg          | sgd-linear | 0.7503 |  0.6387 | 0.7423 | 0.4847 | 0.7235 |    0.7423 |
| Cognitive_Test_Scores | dummy      | 0.5521 |  0.543  | 0.5496 | 0.4683 | 0.5465 |    0.5496 |
| Weight                | sgd-linear | 0.5438 |  0.5413 | 0.5355 | 0.2863 | 0.491  |    0.5355 |
| BloodOxygenLevel      | dummy      | 0.524  |  0.5    | 0.524  | 0.525  | 0.5228 |    0.524  |
| AlcoholLevel          | sgd-linear | 0.5237 |  0.5486 | 0.5147 | 0.2217 | 0.4436 |    0.5147 |
| BodyTemperature       | dummy      | 0.5205 |  0.5479 | 0.5212 | 0.5347 | 0.5186 |    0.5212 |
| AlcoholLevel          | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| HeartRate             | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| HeartRate             | sgd-linear | 0.5159 |  0.5721 | 0.5    | 0      | 0.3403 |    0.5    |
| BloodOxygenLevel      | sgd-linear | 0.5159 |  0.5801 | 0.5    | 0      | 0.3403 |    0.5    |
| BodyTemperature       | sgd-linear | 0.5159 |  0.5858 | 0.5    | 0      | 0.3403 |    0.5    |
| Weight                | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Dosage_in_mg          | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Age                   | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Age                   | sgd-linear | 0.5159 |  0.5987 | 0.5    | 0      | 0.3403 |    0.5    |

# Categorical prediction:

| feature                   | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:--------------------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| Prescription              | sgd-linear | 1      |  1      | 1      | 1      | 1      |    1      |
| Depression_Status         | sgd-linear | 0.7855 |  0.7782 | 0.7782 | 0.5563 | 0.77   |    0.7782 |
| APOE_ε4                   | sgd-linear | 0.7265 |  0.7324 | 0.7324 | 0.9187 | 0.7184 |    0.7324 |
| Smoking_Status            | sgd-linear | 0.5987 |  0.6288 | 0.5961 | 0.5307 | 0.5937 |    0.5961 |
| Education_Level           | sgd-linear | 0.5838 |  0.5998 | 0.5732 | 0.2463 | 0.5223 |    0.5732 |
| Family_History            | sgd-linear | 0.5638 |  0.5686 | 0.5643 | 0.5747 | 0.5596 |    0.5643 |
| Chronic_Health_Conditions | sgd-linear | 0.5561 |  0.5594 | 0.5464 | 0.239  | 0.5008 |    0.5464 |
| Nutrition_Diet            | sgd-linear | 0.5441 |  0.5303 | 0.5423 | 0.477  | 0.5323 |    0.5423 |
| Diabetic                  | dummy      | 0.5398 |  0.5766 | 0.5388 | 0.5083 | 0.5361 |    0.5388 |
| APOE_ε4                   | dummy      | 0.5392 |  0.5556 | 0.5384 | 0.523  | 0.5369 |    0.5384 |
| Dominant_Hand             | sgd-linear | 0.5318 |  0.5277 | 0.5267 | 0.4073 | 0.4922 |    0.5267 |
| Sleep_Quality             | dummy      | 0.5315 |  0.5245 | 0.5303 | 0.4837 | 0.5289 |    0.5303 |
| Chronic_Health_Conditions | dummy      | 0.5278 |  0.5723 | 0.5258 | 0.4823 | 0.5198 |    0.5258 |
| Education_Level           | dummy      | 0.5199 |  0.5    | 0.5211 | 0.5577 | 0.5183 |    0.5211 |
| Depression_Status         | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Family_History            | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Medication_History        | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Medication_History        | sgd-linear | 0.5159 |  0.5434 | 0.5    | 0      | 0.3403 |    0.5    |
| Diabetic                  | sgd-linear | 0.5159 |  0.5668 | 0.5    | 0      | 0.3403 |    0.5    |
| Dominant_Hand             | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Physical_Activity         | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Physical_Activity         | sgd-linear | 0.5159 |  0.5704 | 0.5    | 0      | 0.3403 |    0.5    |
| Prescription              | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Sleep_Quality             | sgd-linear | 0.5159 |  0.5539 | 0.5    | 0      | 0.3403 |    0.5    |
| Smoking_Status            | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Nutrition_Diet            | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |

acc: accuracy
auroc: area under the receiving operater characteristic curve
sens: sensitivity
spec: specificity
