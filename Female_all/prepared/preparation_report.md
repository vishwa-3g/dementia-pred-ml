# Data Preparation Summary

Task:                   Classification
Data original shape:    504 samples × 23 features
Data final shape:       504 samples × 38 features
Target feature:         Dementia

Samples dropped due to NaN target: 0
Indicator variables added for continuous NaNs: 1

# Processing Times

| computation          |   runtime (ms) |
|:---------------------|---------------:|
| unify_nans           |             19 |
| convert_categoricals |              8 |
| inspect_target       |              4 |
| drop_target_nans     |              3 |
| encode_target        |              5 |
| drop_unusable        |             17 |
| deflate_categoricals |              0 |
| encode_categoricals  |             68 |