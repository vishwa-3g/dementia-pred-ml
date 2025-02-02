# Continuous predictions

| feature               | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:----------------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| Cognitive_Test_Scores | sgd-linear | 1      |  1      | 1      | 1      | 1      |    1      |
| Dosage_in_mg          | sgd-linear | 0.735  |  0.548  | 0.7267 | 0.4533 | 0.7089 |    0.7267 |
| Weight                | sgd-linear | 0.55   |  0.5428 | 0.5459 | 0.3988 | 0.5366 |    0.5459 |
| BloodOxygenLevel      | sgd-linear | 0.545  |  0.5556 | 0.5424 | 0.4504 | 0.5391 |    0.5424 |
| AlcoholLevel          | sgd-linear | 0.5383 |  0.5259 | 0.5311 | 0.2919 | 0.5058 |    0.5311 |
| AlcoholLevel          | dummy      | 0.5317 |  0.5    | 0.5312 | 0.5154 | 0.5309 |    0.5312 |
| Age                   | dummy      | 0.53   |  0.5237 | 0.5292 | 0.5015 | 0.528  |    0.5292 |
| Age                   | sgd-linear | 0.52   |  0.5444 | 0.5103 | 0.2089 | 0.4422 |    0.5103 |
| HeartRate             | sgd-linear | 0.5183 |  0.5385 | 0.506  | 0.1027 | 0.3963 |    0.506  |
| BloodOxygenLevel      | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| BodyTemperature       | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| BodyTemperature       | sgd-linear | 0.515  |  0.5618 | 0.5    | 0      | 0.3399 |    0.5    |
| Weight                | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| MRI_Delay             | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| MRI_Delay             | sgd-linear | 0.515  |  0.5383 | 0.5    | 0      | 0.3399 |    0.5    |
| Dosage_in_mg          | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| HeartRate             | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Cognitive_Test_Scores | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |

# Categorical prediction:

| feature                   | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:--------------------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| Prescription              | sgd-linear | 1      |  1      | 1      | 1      | 1      |    1      |
| Depression_Status         | sgd-linear | 0.7767 |  0.7697 | 0.7697 | 0.5395 | 0.7611 |    0.7697 |
| APOE_ε4                   | sgd-linear | 0.6817 |  0.6876 | 0.6876 | 0.89   | 0.6702 |    0.6876 |
| Education_Level           | sgd-linear | 0.5833 |  0.6077 | 0.5818 | 0.5392 | 0.5801 |    0.5818 |
| Smoking_Status            | sgd-linear | 0.5717 |  0.5518 | 0.5842 | 1      | 0.4894 |    0.5842 |
| Smoking_Status            | dummy      | 0.5483 |  0.5    | 0.5487 | 0.56   | 0.548  |    0.5487 |
| Family_History            | sgd-linear | 0.5467 |  0.5457 | 0.5457 | 0.512  | 0.545  |    0.5457 |
| Gender                    | dummy      | 0.5433 |  0.5    | 0.5427 | 0.5221 | 0.5424 |    0.5427 |
| Depression_Status         | dummy      | 0.5383 |  0.5506 | 0.5383 | 0.5362 | 0.5378 |    0.5383 |
| Sleep_Quality             | dummy      | 0.5367 |  0.5359 | 0.5362 | 0.5189 | 0.5359 |    0.5362 |
| APOE_ε4                   | dummy      | 0.53   |  0.5    | 0.5308 | 0.5601 | 0.5292 |    0.5308 |
| Family_History            | dummy      | 0.5217 |  0.5    | 0.5221 | 0.536  | 0.5198 |    0.5221 |
| Nutrition_Diet            | sgd-linear | 0.52   |  0.5418 | 0.5125 | 0.2677 | 0.4693 |    0.5125 |
| Physical_Activity         | dummy      | 0.5183 |  0.5396 | 0.5194 | 0.5565 | 0.5172 |    0.5194 |
| Physical_Activity         | sgd-linear | 0.5183 |  0.525  | 0.5123 | 0.2828 | 0.471  |    0.5123 |
| Chronic_Health_Conditions | dummy      | 0.5183 |  0.5291 | 0.5185 | 0.5226 | 0.5174 |    0.5185 |
| Education_Level           | dummy      | 0.5167 |  0.5361 | 0.5164 | 0.512  | 0.5152 |    0.5164 |
| Diabetic                  | sgd-linear | 0.515  |  0.5423 | 0.5    | 0      | 0.3399 |    0.5    |
| Diabetic                  | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Sleep_Quality             | sgd-linear | 0.515  |  0.5486 | 0.5    | 0      | 0.3399 |    0.5    |
| Medication_History        | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Medication_History        | sgd-linear | 0.515  |  0.5237 | 0.5051 | 0.2085 | 0.4094 |    0.5051 |
| Dominant_Hand             | sgd-linear | 0.515  |  0.5315 | 0.5    | 0      | 0.3399 |    0.5    |
| Dominant_Hand             | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Chronic_Health_Conditions | sgd-linear | 0.515  |  0.5434 | 0.5    | 0      | 0.3399 |    0.5    |
| Prescription              | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Nutrition_Diet            | dummy      | 0.515  |  0.5    | 0.5    | 0      | 0.3399 |    0.5    |
| Gender                    | sgd-linear | 0.515  |  0.551  | 0.5    | 0      | 0.3399 |    0.5    |

acc: accuracy
auroc: area under the receiving operater characteristic curve
sens: sensitivity
spec: specificity
