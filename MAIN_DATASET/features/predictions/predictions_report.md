# Continuous predictions

| feature               | model      |    acc |   auroc |   sens |    spec |     f1 |   bal_acc |
|:----------------------|:-----------|-------:|--------:|-------:|--------:|-------:|----------:|
| Cognitive_Test_Scores | sgd-linear | 1      |  1      | 1      | 1       | 1      |    1      |
| Dosage_in_mg          | sgd-linear | 0.735  |  0.548  | 0.7267 | 0.4533  | 0.7089 |    0.7267 |
| Weight                | sgd-linear | 0.5533 |  0.5428 | 0.549  | 0.3987  | 0.5396 |    0.549  |
| BloodOxygenLevel      | sgd-linear | 0.5483 |  0.5556 | 0.545  | 0.4231  | 0.5382 |    0.545  |
| AlcoholLevel          | sgd-linear | 0.5383 |  0.5259 | 0.5316 | 0.3057  | 0.509  |    0.5316 |
| Dosage_in_mg          | dummy      | 0.5383 |  0.5    | 0.5376 | 0.5123  | 0.5374 |    0.5376 |
| BloodOxygenLevel      | dummy      | 0.5367 |  0.5495 | 0.5363 | 0.5224  | 0.5357 |    0.5363 |
| Weight                | dummy      | 0.5283 |  0.5287 | 0.5275 | 0.505   | 0.5271 |    0.5275 |
| HeartRate             | sgd-linear | 0.5217 |  0.5385 | 0.5088 | 0.08229 | 0.3913 |    0.5088 |
| Age                   | sgd-linear | 0.5167 |  0.5444 | 0.5078 | 0.223   | 0.4523 |    0.5078 |
| AlcoholLevel          | dummy      | 0.515  |  0.5    | 0.5    | 0       | 0.3399 |    0.5    |
| HeartRate             | dummy      | 0.515  |  0.5    | 0.5    | 0       | 0.3399 |    0.5    |
| BodyTemperature       | dummy      | 0.515  |  0.5    | 0.5    | 0       | 0.3399 |    0.5    |
| BodyTemperature       | sgd-linear | 0.515  |  0.5618 | 0.5    | 0       | 0.3399 |    0.5    |
| Age                   | dummy      | 0.515  |  0.5    | 0.5    | 0       | 0.3399 |    0.5    |
| Cognitive_Test_Scores | dummy      | 0.515  |  0.5    | 0.5    | 0       | 0.3399 |    0.5    |

# Categorical prediction:

| feature                   | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:--------------------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| Prescription              | sgd-linear | 1      |  1      | 1      | 1      | 1      |    1      |
| Depression_Status         | sgd-linear | 0.7767 |  0.7697 | 0.7697 | 0.5395 | 0.7611 |    0.7697 |
| APOE_ε4                   | sgd-linear | 0.6817 |  0.6876 | 0.6876 | 0.89   | 0.6702 |    0.6876 |
| Education_Level           | sgd-linear | 0.5833 |  0.6077 | 0.5818 | 0.5392 | 0.5801 |    0.5818 |
| Smoking_Status            | sgd-linear | 0.5717 |  0.5856 | 0.5842 | 1      | 0.4894 |    0.5842 |
| Family_History            | sgd-linear | 0.5467 |  0.5457 | 0.5457 | 0.512  | 0.545  |    0.5457 |
| Family_History            | dummy      | 0.5383 |  0.5532 | 0.5389 | 0.5534 | 0.538  |    0.5389 |
| Education_Level           | dummy      | 0.525  |  0.5    | 0.5249 | 0.5189 | 0.5238 |    0.5249 |
| Nutrition_Diet            | dummy      | 0.5233 |  0.5356 | 0.5226 | 0.495  | 0.5217 |    0.5226 |
| Medication_History        | sgd-linear | 0.52   |  0.5237 | 0.5172 | 0.4327 | 0.4847 |    0.5172 |
| Smoking_Status            | dummy      | 0.5183 |  0.5272 | 0.5167 | 0.4573 | 0.5154 |    0.5167 |
| Physical_Activity         | dummy      | 0.5183 |  0.5    | 0.519  | 0.5463 | 0.5168 |    0.519  |
| Nutrition_Diet            | sgd-linear | 0.5183 |  0.5436 | 0.5118 | 0.2655 | 0.4679 |    0.5118 |
| Physical_Activity         | sgd-linear | 0.5183 |  0.5181 | 0.5131 | 0.3302 | 0.4972 |    0.5131 |
| Depression_Status         | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Gender                    | sgd-linear | 0.515  |  0.551  | 0.5    | 0      | 0.3399 |    0.5    |
| APOE_ε4                   | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Gender                    | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Sleep_Quality             | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Dominant_Hand             | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Diabetic                  | sgd-linear | 0.515  |  0.5423 | 0.5    | 0      | 0.3399 |    0.5    |
| Diabetic                  | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Dominant_Hand             | sgd-linear | 0.515  |  0.5315 | 0.5    | 0      | 0.3399 |    0.5    |
| Medication_History        | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Chronic_Health_Conditions | sgd-linear | 0.515  |  0.5316 | 0.5    | 0      | 0.3399 |    0.5    |
| Chronic_Health_Conditions | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Prescription              | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Sleep_Quality             | sgd-linear | 0.515  |  0.5486 | 0.5    | 0      | 0.3399 |    0.5    |

acc: accuracy
auroc: area under the receiving operater characteristic curve
sens: sensitivity
spec: specificity
