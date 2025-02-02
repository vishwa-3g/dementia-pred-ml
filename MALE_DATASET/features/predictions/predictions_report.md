# Continuous predictions

| feature               | model      |    acc |   auroc |   sens |    spec |     f1 |   bal_acc |
|:----------------------|:-----------|-------:|--------:|-------:|--------:|-------:|----------:|
| Cognitive_Test_Scores | sgd-linear | 1      |  1      | 1      | 1       | 1      |    1      |
| Dosage_in_mg          | sgd-linear | 0.7341 |  0.5417 | 0.726  | 0.452   | 0.7082 |    0.726  |
| BloodOxygenLevel      | sgd-linear | 0.5689 |  0.582  | 0.5677 | 0.5076  | 0.5653 |    0.5677 |
| BodyTemperature       | sgd-linear | 0.5524 |  0.5699 | 0.5513 | 0.4869  | 0.5474 |    0.5513 |
| Age                   | sgd-linear | 0.5522 |  0.569  | 0.5433 | 0.2369  | 0.497  |    0.5433 |
| Weight                | sgd-linear | 0.5456 |  0.5776 | 0.5404 | 0.3608  | 0.5242 |    0.5404 |
| BodyTemperature       | dummy      | 0.5424 |  0.5    | 0.5415 | 0.5212  | 0.5407 |    0.5415 |
| HeartRate             | dummy      | 0.5419 |  0.5    | 0.5399 | 0.4589  | 0.537  |    0.5399 |
| AlcoholLevel          | sgd-linear | 0.5318 |  0.5407 | 0.5188 | 0.08276 | 0.3992 |    0.5188 |
| BloodOxygenLevel      | dummy      | 0.5185 |  0.5279 | 0.5171 | 0.4729  | 0.5135 |    0.5171 |
| AlcoholLevel          | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |
| HeartRate             | sgd-linear | 0.5151 |  0.6018 | 0.5    | 0       | 0.34   |    0.5    |
| Weight                | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |
| Dosage_in_mg          | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |
| Age                   | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |
| Cognitive_Test_Scores | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |

# Categorical prediction:

| feature                   | model      |    acc |   auroc |   sens |    spec |     f1 |   bal_acc |
|:--------------------------|:-----------|-------:|--------:|-------:|--------:|-------:|----------:|
| Prescription              | sgd-linear | 1      |  1      | 1      | 1       | 1      |    1      |
| Depression_Status         | sgd-linear | 0.7576 |  0.75   | 0.75   | 0.5     | 0.7365 |    0.75   |
| APOE_ε4                   | sgd-linear | 0.6633 |  0.6694 | 0.6694 | 0.8677  | 0.6523 |    0.6694 |
| Depression_Status         | dummy      | 0.5893 |  0.569  | 0.5893 | 0.5702  | 0.587  |    0.5893 |
| Education_Level           | dummy      | 0.5855 |  0.5    | 0.5853 | 0.5823  | 0.5836 |    0.5853 |
| Smoking_Status            | sgd-linear | 0.5755 |  0.5531 | 0.5878 | 1       | 0.4935 |    0.5878 |
| Education_Level           | sgd-linear | 0.5693 |  0.5764 | 0.5696 | 0.57    | 0.569  |    0.5696 |
| Chronic_Health_Conditions | dummy      | 0.5589 |  0.5436 | 0.5577 | 0.5485  | 0.5551 |    0.5577 |
| Family_History            | sgd-linear | 0.5526 |  0.5983 | 0.552  | 0.5283  | 0.5508 |    0.552  |
| Dominant_Hand             | dummy      | 0.5524 |  0.5406 | 0.5509 | 0.5074  | 0.5498 |    0.5509 |
| Medication_History        | dummy      | 0.5422 |  0.5516 | 0.5402 | 0.4727  | 0.5376 |    0.5402 |
| Physical_Activity         | sgd-linear | 0.5389 |  0.5329 | 0.5345 | 0.3687  | 0.5201 |    0.5345 |
| Sleep_Quality             | dummy      | 0.5321 |  0.5473 | 0.5311 | 0.4869  | 0.5285 |    0.5311 |
| Diabetic                  | dummy      | 0.5186 |  0.5323 | 0.5182 | 0.4803  | 0.5151 |    0.5182 |
| Chronic_Health_Conditions | sgd-linear | 0.5185 |  0.5318 | 0.5143 | 0.397   | 0.4673 |    0.5143 |
| Nutrition_Diet            | sgd-linear | 0.5185 |  0.556  | 0.5077 | 0.09286 | 0.3786 |    0.5077 |
| Diabetic                  | sgd-linear | 0.5185 |  0.5373 | 0.5061 | 0.08966 | 0.3776 |    0.5061 |
| Sleep_Quality             | sgd-linear | 0.5153 |  0.5398 | 0.5123 | 0.3214  | 0.4466 |    0.5123 |
| Physical_Activity         | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |
| APOE_ε4                   | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |
| Dominant_Hand             | sgd-linear | 0.5151 |  0.5467 | 0.5    | 0       | 0.34   |    0.5    |
| Prescription              | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |
| Smoking_Status            | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |
| Medication_History        | sgd-linear | 0.5151 |  0.5517 | 0.5    | 0       | 0.34   |    0.5    |
| Family_History            | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |
| Nutrition_Diet            | dummy      | 0.5151 |  0.5    | 0.5    | 0       | 0.34   |    0.5    |

acc: accuracy
auroc: area under the receiving operater characteristic curve
sens: sensitivity
spec: specificity
