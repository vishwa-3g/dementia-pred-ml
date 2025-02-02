# Continuous predictions

| feature               | model      |    acc |   auroc |   sens |    spec |     f1 |   bal_acc |
|:----------------------|:-----------|-------:|--------:|-------:|--------:|-------:|----------:|
| Cognitive_Test_Scores | sgd-linear | 1      |  1      | 1      | 1       | 1      |    1      |
| Dosage_in_mg          | sgd-linear | 0.7096 |  0.575  | 0.7    | 0.4     | 0.6752 |    0.7    |
| BodyTemperature       | sgd-linear | 0.5802 |  0.6053 | 0.5793 | 0.5583  | 0.5768 |    0.5793 |
| Dosage_in_mg          | dummy      | 0.565  |  0.5335 | 0.5642 | 0.5417  | 0.562  |    0.5642 |
| BloodOxygenLevel      | sgd-linear | 0.5606 |  0.5752 | 0.5563 | 0.4     | 0.5426 |    0.5563 |
| AlcoholLevel          | dummy      | 0.5527 |  0.5764 | 0.5512 | 0.5     | 0.5493 |    0.5512 |
| Age                   | sgd-linear | 0.5521 |  0.5646 | 0.5422 | 0.2417  | 0.4978 |    0.5422 |
| Weight                | sgd-linear | 0.5485 |  0.5435 | 0.54   | 0.2917  | 0.5031 |    0.54   |
| Weight                | dummy      | 0.5438 |  0.5    | 0.5443 | 0.5667  | 0.5425 |    0.5443 |
| Cognitive_Test_Scores | dummy      | 0.5404 |  0.5409 | 0.5388 | 0.5     | 0.5361 |    0.5388 |
| BloodOxygenLevel      | dummy      | 0.5239 |  0.5    | 0.5246 | 0.5583  | 0.5221 |    0.5246 |
| HeartRate             | sgd-linear | 0.5202 |  0.5639 | 0.515  | 0.325   | 0.4787 |    0.515  |
| Age                   | dummy      | 0.5201 |  0.5    | 0.5202 | 0.5417  | 0.5168 |    0.5202 |
| AlcoholLevel          | sgd-linear | 0.5161 |  0.5658 | 0.5032 | 0.08333 | 0.3746 |    0.5032 |
| HeartRate             | dummy      | 0.5161 |  0.5    | 0.5    | 0       | 0.3404 |    0.5    |
| BodyTemperature       | dummy      | 0.5161 |  0.5    | 0.5    | 0       | 0.3404 |    0.5    |

# Categorical prediction:

| feature                   | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:--------------------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| Prescription              | sgd-linear | 1      |  1      | 1      | 1      | 1      |    1      |
| Depression_Status         | sgd-linear | 0.75   |  0.7417 | 0.7417 | 0.4833 | 0.7258 |    0.7417 |
| APOE_ε4                   | sgd-linear | 0.6531 |  0.6595 | 0.6595 | 0.8583 | 0.6405 |    0.6595 |
| Smoking_Status            | sgd-linear | 0.6089 |  0.5944 | 0.6211 | 1      | 0.5473 |    0.6211 |
| Smoking_Status            | dummy      | 0.5639 |  0.5    | 0.5625 | 0.5417 | 0.5604 |    0.5625 |
| Education_Level           | sgd-linear | 0.5608 |  0.5849 | 0.55   | 0.2167 | 0.4971 |    0.55   |
| Physical_Activity         | sgd-linear | 0.5608 |  0.5778 | 0.5552 | 0.3833 | 0.5408 |    0.5552 |
| Nutrition_Diet            | dummy      | 0.5566 |  0.5    | 0.5548 | 0.5    | 0.5534 |    0.5548 |
| Depression_Status         | dummy      | 0.5563 |  0.5    | 0.5556 | 0.55   | 0.5543 |    0.5556 |
| Sleep_Quality             | dummy      | 0.5363 |  0.5    | 0.5343 | 0.4667 | 0.5329 |    0.5343 |
| APOE_ε4                   | dummy      | 0.533  |  0.5    | 0.5331 | 0.5333 | 0.5314 |    0.5331 |
| Sleep_Quality             | sgd-linear | 0.5324 |  0.5493 | 0.5327 | 0.5333 | 0.5308 |    0.5327 |
| Physical_Activity         | dummy      | 0.5321 |  0.5    | 0.5317 | 0.5167 | 0.5306 |    0.5317 |
| Education_Level           | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Family_History            | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Dominant_Hand             | sgd-linear | 0.5161 |  0.5551 | 0.5    | 0      | 0.3404 |    0.5    |
| Medication_History        | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Medication_History        | sgd-linear | 0.5161 |  0.5245 | 0.5    | 0      | 0.3404 |    0.5    |
| Dominant_Hand             | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Nutrition_Diet            | sgd-linear | 0.5161 |  0.5556 | 0.5    | 0      | 0.3404 |    0.5    |
| Diabetic                  | sgd-linear | 0.5161 |  0.5657 | 0.5    | 0      | 0.3404 |    0.5    |
| Prescription              | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Diabetic                  | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Chronic_Health_Conditions | sgd-linear | 0.5161 |  0.5879 | 0.5    | 0      | 0.3404 |    0.5    |
| Chronic_Health_Conditions | dummy      | 0.5161 |  0.5    | 0.5    | 0      | 0.3404 |    0.5    |
| Family_History            | sgd-linear | 0.5161 |  0.561  | 0.5    | 0      | 0.3404 |    0.5    |

acc: accuracy
auroc: area under the receiving operater characteristic curve
sens: sensitivity
spec: specificity
