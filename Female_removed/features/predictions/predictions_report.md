# Continuous predictions

| feature          | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:-----------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| Age              | dummy      | 0.5475 |  0.5276 | 0.5466 | 0.5087 | 0.5419 |    0.5466 |
| Weight           | sgd-linear | 0.5398 |  0.5413 | 0.5294 | 0.2127 | 0.4705 |    0.5294 |
| Weight           | dummy      | 0.5193 |  0.5    | 0.5181 | 0.4977 | 0.5162 |    0.5181 |
| AlcoholLevel     | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| AlcoholLevel     | sgd-linear | 0.5159 |  0.5486 | 0.5    | 0      | 0.3403 |    0.5    |
| HeartRate        | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| HeartRate        | sgd-linear | 0.5159 |  0.5721 | 0.5    | 0      | 0.3403 |    0.5    |
| BloodOxygenLevel | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| BloodOxygenLevel | sgd-linear | 0.5159 |  0.5801 | 0.5    | 0      | 0.3403 |    0.5    |
| BodyTemperature  | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| BodyTemperature  | sgd-linear | 0.5159 |  0.5858 | 0.5    | 0      | 0.3403 |    0.5    |
| Age              | sgd-linear | 0.5159 |  0.5987 | 0.5    | 0      | 0.3403 |    0.5    |

# Categorical prediction:

| feature                   | model      |    acc |   auroc |   sens |   spec |     f1 |   bal_acc |
|:--------------------------|:-----------|-------:|--------:|-------:|-------:|-------:|----------:|
| Depression_Status         | sgd-linear | 0.7855 |  0.7782 | 0.7782 | 0.5563 | 0.77   |    0.7782 |
| APOE_ε4                   | sgd-linear | 0.7265 |  0.7324 | 0.7324 | 0.9187 | 0.7184 |    0.7324 |
| Smoking_Status            | sgd-linear | 0.5987 |  0.6288 | 0.5961 | 0.5307 | 0.5937 |    0.5961 |
| Education_Level           | sgd-linear | 0.5838 |  0.5998 | 0.5732 | 0.2463 | 0.5223 |    0.5732 |
| Family_History            | sgd-linear | 0.5638 |  0.5686 | 0.5643 | 0.5747 | 0.5596 |    0.5643 |
| Sleep_Quality             | dummy      | 0.5594 |  0.5481 | 0.5589 | 0.5487 | 0.5581 |    0.5589 |
| Nutrition_Diet            | sgd-linear | 0.5481 |  0.5512 | 0.5433 | 0.402  | 0.5358 |    0.5433 |
| Chronic_Health_Conditions | sgd-linear | 0.5281 |  0.5424 | 0.5221 | 0.3057 | 0.4803 |    0.5221 |
| Dominant_Hand             | sgd-linear | 0.5278 |  0.5277 | 0.5264 | 0.499  | 0.5234 |    0.5264 |
| Medication_History        | dummy      | 0.5204 |  0.5    | 0.5213 | 0.535  | 0.5166 |    0.5213 |
| Chronic_Health_Conditions | dummy      | 0.5202 |  0.5594 | 0.52   | 0.517  | 0.5147 |    0.52   |
| Nutrition_Diet            | dummy      | 0.5199 |  0.5205 | 0.52   | 0.5247 | 0.5176 |    0.52   |
| Family_History            | dummy      | 0.5195 |  0.5    | 0.5194 | 0.5233 | 0.5147 |    0.5194 |
| Education_Level           | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Dominant_Hand             | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Medication_History        | sgd-linear | 0.5159 |  0.5434 | 0.5    | 0      | 0.3403 |    0.5    |
| Diabetic                  | sgd-linear | 0.5159 |  0.5668 | 0.5    | 0      | 0.3403 |    0.5    |
| Diabetic                  | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Physical_Activity         | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Depression_Status         | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Sleep_Quality             | sgd-linear | 0.5159 |  0.5539 | 0.5    | 0      | 0.3403 |    0.5    |
| Smoking_Status            | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| APOE_ε4                   | dummy      | 0.5159 |  0.5    | 0.5    | 0      | 0.3403 |    0.5    |
| Physical_Activity         | sgd-linear | 0.5118 |  0.5579 | 0.5044 | 0.2473 | 0.4587 |    0.5044 |

acc: accuracy
auroc: area under the receiving operater characteristic curve
sens: sensitivity
spec: specificity
