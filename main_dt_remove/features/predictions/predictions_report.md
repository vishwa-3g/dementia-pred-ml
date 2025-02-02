# Continuous predictions

| feature          | model      |   acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:-----------------|:-----------|------:|--------:|-------:|-------:|-------:|----------:|
| BloodOxygenLevel | sgd-linear | 0.548 |  0.557  | 0.5451 | 0.4321 | 0.5399 |    0.5451 |
| Weight           | sgd-linear | 0.546 |  0.5349 | 0.5426 | 0.4196 | 0.5348 |    0.5426 |
| BloodOxygenLevel | dummy      | 0.538 |  0.5    | 0.5387 | 0.5638 | 0.5364 |    0.5387 |
| BodyTemperature  | sgd-linear | 0.536 |  0.5455 | 0.5339 | 0.4648 | 0.5324 |    0.5339 |
| AlcoholLevel     | sgd-linear | 0.532 |  0.5366 | 0.5285 | 0.3751 | 0.5149 |    0.5285 |
| Age              | sgd-linear | 0.532 |  0.5341 | 0.5278 | 0.3662 | 0.5152 |    0.5278 |
| Age              | dummy      | 0.53  |  0.5177 | 0.5301 | 0.527  | 0.5267 |    0.5301 |
| AlcoholLevel     | dummy      | 0.53  |  0.5    | 0.5302 | 0.531  | 0.5297 |    0.5302 |
| HeartRate        | dummy      | 0.514 |  0.5    | 0.5    | 0      | 0.3395 |    0.5    |
| HeartRate        | sgd-linear | 0.514 |  0.5489 | 0.5    | 0      | 0.3395 |    0.5    |
| BodyTemperature  | dummy      | 0.514 |  0.5    | 0.5    | 0      | 0.3395 |    0.5    |
| Weight           | dummy      | 0.514 |  0.5    | 0.5    | 0      | 0.3395 |    0.5    |

# Categorical prediction:

| feature                   | model      |   acc |   auroc |   sens |    spec |     f1 |   bal_acc |
|:--------------------------|:-----------|------:|--------:|-------:|--------:|-------:|----------:|
| Depression_Status         | sgd-linear | 0.77  |  0.7633 | 0.7633 | 0.5265  | 0.7528 |    0.7633 |
| APOE_ε4                   | sgd-linear | 0.688 |  0.6935 | 0.6935 | 0.885   | 0.6772 |    0.6935 |
| Education_Level           | sgd-linear | 0.578 |  0.567  | 0.5689 | 0.2432  | 0.5214 |    0.5689 |
| Smoking_Status            | sgd-linear | 0.576 |  0.621  | 0.574  | 0.5218  | 0.5718 |    0.574  |
| Family_History            | dummy      | 0.55  |  0.5327 | 0.5497 | 0.5389  | 0.5494 |    0.5497 |
| Physical_Activity         | dummy      | 0.534 |  0.5438 | 0.5342 | 0.5552  | 0.5322 |    0.5342 |
| Family_History            | sgd-linear | 0.532 |  0.5473 | 0.5315 | 0.5104  | 0.531  |    0.5315 |
| Diabetic                  | dummy      | 0.532 |  0.5    | 0.5317 | 0.5187  | 0.5311 |    0.5317 |
| Physical_Activity         | sgd-linear | 0.526 |  0.5297 | 0.522  | 0.3747  | 0.5128 |    0.522  |
| Medication_History        | dummy      | 0.522 |  0.5373 | 0.5205 | 0.4693  | 0.5195 |    0.5205 |
| Nutrition_Diet            | sgd-linear | 0.518 |  0.5211 | 0.5055 | 0.08163 | 0.3763 |    0.5055 |
| Gender                    | dummy      | 0.518 |  0.5332 | 0.5181 | 0.5267  | 0.5176 |    0.5181 |
| Depression_Status         | dummy      | 0.516 |  0.5    | 0.5154 | 0.4981  | 0.5138 |    0.5154 |
| Chronic_Health_Conditions | sgd-linear | 0.516 |  0.5617 | 0.5133 | 0.4037  | 0.4718 |    0.5133 |
| Smoking_Status            | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Sleep_Quality             | sgd-linear | 0.514 |  0.5213 | 0.5    | 0       | 0.3395 |    0.5    |
| Sleep_Quality             | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Chronic_Health_Conditions | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| APOE_ε4                   | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Nutrition_Diet            | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Medication_History        | sgd-linear | 0.514 |  0.5442 | 0.5    | 0       | 0.3395 |    0.5    |
| Dominant_Hand             | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Education_Level           | dummy      | 0.514 |  0.5    | 0.5    | 0       | 0.3395 |    0.5    |
| Dominant_Hand             | sgd-linear | 0.514 |  0.5255 | 0.5    | 0       | 0.3395 |    0.5    |
| Gender                    | sgd-linear | 0.502 |  0.5538 | 0.4928 | 0.1125  | 0.3624 |    0.4928 |
| Diabetic                  | sgd-linear | 0.49  |  0.5639 | 0.48   | 0.07917 | 0.351  |    0.48   |

acc: accuracy
auroc: area under the receiving operater characteristic curve
sens: sensitivity
spec: specificity
