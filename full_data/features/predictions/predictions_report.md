# Continuous predictions

| feature               | model      |   acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:----------------------|:-----------|------:|--------:|-------:|-------:|-------:|----------:|
| Cognitive_Test_Scores | sgd-linear | 1     |  1      | 1      | 1      | 1      |    1      |
| Dosage_in_mg          | sgd-linear | 0.74  |  0.5701 | 0.7326 | 0.4652 | 0.7153 |    0.7326 |
| HeartRate             | dummy      | 0.552 |  0.5    | 0.5528 | 0.5686 | 0.5506 |    0.5528 |
| Weight                | sgd-linear | 0.548 |  0.5349 | 0.542  | 0.3252 | 0.5143 |    0.542  |
| BloodOxygenLevel      | sgd-linear | 0.546 |  0.557  | 0.5435 | 0.4485 | 0.5394 |    0.5435 |
| AlcoholLevel          | sgd-linear | 0.536 |  0.5366 | 0.5329 | 0.4075 | 0.5259 |    0.5329 |
| BodyTemperature       | sgd-linear | 0.532 |  0.5455 | 0.5287 | 0.4034 | 0.5213 |    0.5287 |
| BloodOxygenLevel      | dummy      | 0.53  |  0.5243 | 0.5287 | 0.4895 | 0.5266 |    0.5287 |
| AlcoholLevel          | dummy      | 0.514 |  0.5    | 0.5    | 0      | 0.3395 |    0.5    |
| HeartRate             | sgd-linear | 0.514 |  0.5489 | 0.5    | 0      | 0.3395 |    0.5    |
| BodyTemperature       | dummy      | 0.514 |  0.5    | 0.5    | 0      | 0.3395 |    0.5    |
| Weight                | dummy      | 0.514 |  0.5    | 0.5    | 0      | 0.3395 |    0.5    |
| Dosage_in_mg          | dummy      | 0.514 |  0.5    | 0.5    | 0      | 0.3395 |    0.5    |
| Age                   | dummy      | 0.514 |  0.5    | 0.5    | 0      | 0.3395 |    0.5    |
| Age                   | sgd-linear | 0.514 |  0.5341 | 0.5099 | 0.35   | 0.4971 |    0.5099 |
| Cognitive_Test_Scores | dummy      | 0.514 |  0.5    | 0.5    | 0      | 0.3395 |    0.5    |

# Categorical prediction:

| feature                   | model      |   acc |   auroc |   sens |    spec |     f1 |   bal_acc |
|:--------------------------|:-----------|------:|--------:|-------:|--------:|-------:|----------:|
| Prescription              | sgd-linear | 1     |  1      | 1      | 1       | 1      |    1      |
| Depression_Status         | sgd-linear | 0.77  |  0.7633 | 0.7633 | 0.5265  | 0.7528 |    0.7633 |
| APOE_ε4                   | sgd-linear | 0.688 |  0.6935 | 0.6935 | 0.885   | 0.6772 |    0.6935 |
| Education_Level           | sgd-linear | 0.578 |  0.567  | 0.5689 | 0.2432  | 0.5214 |    0.5689 |
| Smoking_Status            | sgd-linear | 0.576 |  0.621  | 0.574  | 0.5218  | 0.5718 |    0.574  |
| Medication_History        | dummy      | 0.54  |  0.5    | 0.5389 | 0.5062  | 0.538  |    0.5389 |
| Chronic_Health_Conditions | dummy      | 0.54  |  0.5352 | 0.5391 | 0.506   | 0.5382 |    0.5391 |
| Dominant_Hand             | dummy      | 0.536 |  0.5    | 0.5362 | 0.5394  | 0.5354 |    0.5362 |
| Family_History            | sgd-linear | 0.532 |  0.5473 | 0.5315 | 0.5104  | 0.531  |    0.5315 |
| Diabetic                  | dummy      | 0.528 |  0.5    | 0.529  | 0.588   | 0.5241 |    0.529  |
| Physical_Activity         | sgd-linear | 0.526 |  0.5296 | 0.522  | 0.3747  | 0.5128 |    0.522  |
| Sleep_Quality             | dummy      | 0.524 |  0.5224 | 0.524  | 0.5188  | 0.523  |    0.524  |
| Family_History            | dummy      | 0.522 |  0.5441 | 0.5208 | 0.477   | 0.5202 |    0.5208 |
| Sleep_Quality             | sgd-linear | 0.514 |  0.5213 | 0.5    | 0       | 0.3395 |    0.5    |
| Nutrition_Diet            | sgd-linear | 0.514 |  0.5462 | 0.5    | 0       | 0.3395 |    0.5    |
| Prescription              | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Smoking_Status            | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Physical_Activity         | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| APOE_ε4                   | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Nutrition_Diet            | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Medication_History        | sgd-linear | 0.514 |  0.5442 | 0.5    | 0       | 0.3395 |    0.5    |
| Education_Level           | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Dominant_Hand             | sgd-linear | 0.514 |  0.5255 | 0.5    | 0       | 0.3395 |    0.5    |
| Diabetic                  | sgd-linear | 0.514 |  0.5639 | 0.5    | 0       | 0.3395 |    0.5    |
| Depression_Status         | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Gender                    | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Chronic_Health_Conditions | sgd-linear | 0.504 |  0.5535 | 0.4908 | 0.02857 | 0.3516 |    0.4908 |
| Gender                    | sgd-linear | 0.502 |  0.5538 | 0.4928 | 0.1125  | 0.3624 |    0.4928 |

acc: accuracy
auroc: area under the receiving operater characteristic curve
sens: sensitivity
spec: specificity
