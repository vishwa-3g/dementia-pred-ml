# Continuous predictions

| feature               | model      |    acc |   auroc |   sens |    spec |     f1 |   bal_acc |
|:----------------------|:-----------|-------:|--------:|-------:|--------:|-------:|----------:|
| Cognitive_Test_Scores | sgd-linear | 1      |  1      | 1      | 1       | 1      |    1      |
| Dosage_in_mg          | sgd-linear | 0.7186 |  0.5586 | 0.7089 | 0.4177  | 0.6851 |    0.7089 |
| AlcoholLevel          | dummy      | 0.5496 |  0.552  | 0.5495 | 0.5416  | 0.5482 |    0.5495 |
| Weight                | sgd-linear | 0.5464 |  0.5856 | 0.5418 | 0.4044  | 0.5303 |    0.5418 |
| BodyTemperature       | dummy      | 0.5463 |  0.5    | 0.5461 | 0.5483  | 0.5453 |    0.5461 |
| HeartRate             | sgd-linear | 0.5432 |  0.564  | 0.5373 | 0.3366  | 0.5146 |    0.5373 |
| Cognitive_Test_Scores | dummy      | 0.543  |  0.5729 | 0.5425 | 0.528   | 0.5419 |    0.5425 |
| BloodOxygenLevel      | dummy      | 0.5336 |  0.5    | 0.5332 | 0.5211  | 0.5318 |    0.5332 |
| Dosage_in_mg          | dummy      | 0.5302 |  0.5    | 0.5318 | 0.5834  | 0.5295 |    0.5318 |
| BodyTemperature       | sgd-linear | 0.5263 |  0.5849 | 0.522  | 0.3963  | 0.5101 |    0.522  |
| HeartRate             | dummy      | 0.5231 |  0.576  | 0.5227 | 0.5064  | 0.5213 |    0.5227 |
| Age                   | sgd-linear | 0.5198 |  0.5392 | 0.5038 | 0.01379 | 0.3532 |    0.5038 |
| BloodOxygenLevel      | sgd-linear | 0.5197 |  0.556  | 0.5122 | 0.2945  | 0.4811 |    0.5122 |
| AlcoholLevel          | sgd-linear | 0.5166 |  0.5794 | 0.5    | 0       | 0.3406 |    0.5    |
| Weight                | dummy      | 0.5166 |  0.5    | 0.5    | 0       | 0.3406 |    0.5    |
| Age                   | dummy      | 0.5166 |  0.5    | 0.5    | 0       | 0.3406 |    0.5    |

# Categorical prediction:

| feature                   | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:--------------------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| Prescription              | sgd-linear | 1      |  1      | 1      | 1      | 1      |    1      |
| Depression_Status         | sgd-linear | 0.7714 |  0.7631 | 0.7631 | 0.5262 | 0.751  |    0.7631 |
| APOE_ε4                   | sgd-linear | 0.7251 |  0.731  | 0.731  | 0.9041 | 0.7187 |    0.731  |
| Education_Level           | sgd-linear | 0.5899 |  0.6243 | 0.5878 | 0.5143 | 0.5858 |    0.5878 |
| Chronic_Health_Conditions | dummy      | 0.5893 |  0.5759 | 0.5886 | 0.5549 | 0.5856 |    0.5886 |
| Dominant_Hand             | dummy      | 0.5697 |  0.5597 | 0.5699 | 0.5759 | 0.5687 |    0.5699 |
| Smoking_Status            | dummy      | 0.5598 |  0.551  | 0.5607 | 0.5825 | 0.5569 |    0.5607 |
| APOE_ε4                   | dummy      | 0.5566 |  0.5    | 0.5556 | 0.528  | 0.5545 |    0.5556 |
| Sleep_Quality             | dummy      | 0.5532 |  0.5828 | 0.555  | 0.6094 | 0.5517 |    0.555  |
| Smoking_Status            | sgd-linear | 0.5531 |  0.5881 | 0.5525 | 0.5214 | 0.5488 |    0.5525 |
| Medication_History        | dummy      | 0.5531 |  0.5274 | 0.5553 | 0.6297 | 0.5489 |    0.5553 |
| Physical_Activity         | sgd-linear | 0.5501 |  0.6014 | 0.5433 | 0.3356 | 0.5248 |    0.5433 |
| Chronic_Health_Conditions | sgd-linear | 0.5464 |  0.5455 | 0.5347 | 0.1848 | 0.475  |    0.5347 |
| Family_History            | dummy      | 0.5431 |  0.5709 | 0.542  | 0.5198 | 0.5411 |    0.542  |
| Family_History            | sgd-linear | 0.5296 |  0.563  | 0.5289 | 0.5264 | 0.5273 |    0.5289 |
| Dominant_Hand             | sgd-linear | 0.5197 |  0.5371 | 0.5215 | 0.5683 | 0.5177 |    0.5215 |
| Diabetic                  | dummy      | 0.5166 |  0.5    | 0.5    | 0      | 0.3406 |    0.5    |
| Diabetic                  | sgd-linear | 0.5166 |  0.5497 | 0.5    | 0      | 0.3406 |    0.5    |
| Depression_Status         | dummy      | 0.5166 |  0.5    | 0.5    | 0      | 0.3406 |    0.5    |
| Medication_History        | sgd-linear | 0.5166 |  0.5464 | 0.5    | 0      | 0.3406 |    0.5    |
| Education_Level           | dummy      | 0.5166 |  0.5    | 0.5    | 0      | 0.3406 |    0.5    |
| Prescription              | dummy      | 0.5166 |  0.5    | 0.5    | 0      | 0.3406 |    0.5    |
| Nutrition_Diet            | sgd-linear | 0.5166 |  0.5375 | 0.5    | 0      | 0.3406 |    0.5    |
| Nutrition_Diet            | dummy      | 0.5166 |  0.5    | 0.5    | 0      | 0.3406 |    0.5    |
| Physical_Activity         | dummy      | 0.5166 |  0.5    | 0.5    | 0      | 0.3406 |    0.5    |
| Sleep_Quality             | sgd-linear | 0.4799 |  0.5782 | 0.4701 | 0.1724 | 0.3735 |    0.4701 |

acc: accuracy
auroc: area under the receiving operater characteristic curve
sens: sensitivity
spec: specificity
