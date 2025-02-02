# Data Preparation Summary

Task:                   Classification
Data original shape:    1000 samples × 22 features
Data final shape:       1000 samples × 51 features
Target feature:         Dementia

Samples dropped due to NaN target: 0
Indicator variables added for continuous NaNs: 1

# Processing Times

| computation          |   runtime (ms) |
|:---------------------|---------------:|
| unify_nans           |             17 |
| convert_categoricals |              2 |
| inspect_target       |              5 |
| drop_target_nans     |              2 |
| encode_target        |              5 |
| drop_unusable        |              0 |
| deflate_categoricals |              0 |
| encode_categoricals  |             18 |