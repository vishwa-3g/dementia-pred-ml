# Data Preparation Summary

Task:                   Classification
Data original shape:    1000 samples × 23 features
Data final shape:       1000 samples × 52 features
Target feature:         Dementia

Samples dropped due to NaN target: 0
Indicator variables added for continuous NaNs: 1

# Processing Times

| computation          |   runtime (ms) |
|:---------------------|---------------:|
| unify_nans           |             15 |
| convert_categoricals |              2 |
| inspect_target       |              2 |
| drop_target_nans     |              1 |
| encode_target        |              3 |
| drop_unusable        |              0 |
| deflate_categoricals |              0 |
| encode_categoricals  |             30 |