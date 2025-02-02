# Continuous predictions

| feature          | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:-----------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| BodyTemperature  | sgd-linear | 0.58   |  0.6053 | 0.5787 | 0.5417 | 0.5759 |    0.5787 |
| Weight           | sgd-linear | 0.5605 |  0.5435 | 0.5547 | 0.375  | 0.5416 |    0.5547 |
| BloodOxygenLevel | sgd-linear | 0.5446 |  0.5752 | 0.5416 | 0.4167 | 0.5278 |    0.5416 |
| BloodOxygenLevel | dummy      | 0.5446 |  0.5483 | 0.5439 | 0.5333 | 0.5432 |    0.5439 |
| Age              | sgd-linear | 0.544  |  0.5646 | 0.5337 | 0.2333 | 0.49   |    0.5337 |
| Age              | dummy      | 0.5364 |  0.5637 | 0.5344 | 0.4833 | 0.5302 |    0.5344 |
| BodyTemperature  | dummy      | 0.5325 |  0.554  | 0.5309 | 0.475  | 0.528  |    0.5309 |
| AlcoholLevel     | dummy      | 0.5242 |  0.5    | 0.5234 | 0.4917 | 0.5209 |    0.5234 |
| AlcoholLevel     | sgd-linear | 0.5161 |  0.5658 | 0.5    | 0      | 0.3404 |    0.5    |
| HeartRate        | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| HeartRate        | sgd-linear | 0.5161 |  0.5639 | 0.5    | 0      | 0.3404 |    0.5    |
| Weight           | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |

# Categorical prediction:

| feature                   | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:--------------------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| Depression_Status         | sgd-linear | 0.75   |  0.7417 | 0.7417 | 0.4833 | 0.7258 |    0.7417 |
| APOE_ε4                   | sgd-linear | 0.6531 |  0.6595 | 0.6595 | 0.8583 | 0.6405 |    0.6595 |
| Smoking_Status            | sgd-linear | 0.6089 |  0.5876 | 0.6211 | 1      | 0.5473 |    0.6211 |
| Education_Level           | dummy      | 0.5649 |  0.5    | 0.566  | 0.5917 | 0.5636 |    0.566  |
| Physical_Activity         | sgd-linear | 0.5608 |  0.59   | 0.5552 | 0.3833 | 0.5408 |    0.5552 |
| Diabetic                  | dummy      | 0.5526 |  0.5421 | 0.5521 | 0.5333 | 0.5516 |    0.5521 |
| Education_Level           | sgd-linear | 0.5487 |  0.5313 | 0.5421 | 0.3417 | 0.5133 |    0.5421 |
| Sleep_Quality             | dummy      | 0.5406 |  0.5    | 0.5408 | 0.55   | 0.5377 |    0.5408 |
| APOE_ε4                   | dummy      | 0.5366 |  0.5551 | 0.5372 | 0.55   | 0.5352 |    0.5372 |
| Sleep_Quality             | sgd-linear | 0.5324 |  0.5493 | 0.5327 | 0.5333 | 0.5308 |    0.5327 |
| Medication_History        | dummy      | 0.5244 |  0.5    | 0.524  | 0.5167 | 0.5216 |    0.524  |
| Medication_History        | sgd-linear | 0.5202 |  0.5245 | 0.5062 | 0.1083 | 0.379  |    0.5062 |
| Dominant_Hand             | sgd-linear | 0.5161 |  0.5551 | 0.5    | 0      | 0.3404 |    0.5    |
| Dominant_Hand             | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Diabetic                  | sgd-linear | 0.5161 |  0.5657 | 0.5022 | 0.1083 | 0.3748 |    0.5022 |
| Depression_Status         | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Family_History            | sgd-linear | 0.5161 |  0.561  | 0.5    | 0      | 0.3404 |    0.5    |
| Nutrition_Diet            | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Nutrition_Diet            | sgd-linear | 0.5161 |  0.5663 | 0.5    | 0      | 0.3404 |    0.5    |
| Physical_Activity         | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Chronic_Health_Conditions | sgd-linear | 0.5161 |  0.5805 | 0.5    | 0      | 0.3404 |    0.5    |
| Chronic_Health_Conditions | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Smoking_Status            | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Family_History            | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |

acc: accuracy
auroc: area under the receiving operater characteristic curve
sens: sensitivity
spec: specificity
