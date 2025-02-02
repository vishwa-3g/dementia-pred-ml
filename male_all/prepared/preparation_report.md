# Data Preparation Summary

Task:                   Classification
Data original shape:    496 samples × 23 features
Data final shape:       496 samples × 38 features
Target feature:         Dementia

Samples dropped due to NaN target: 0
Indicator variables added for continuous NaNs: 1

# Processing Times

| computation          |   runtime (ms) |
|:---------------------|---------------:|
| unify_nans           |             14 |
| convert_categoricals |             20 |
| inspect_target       |              2 |
| drop_target_nans     |              2 |
| encode_target        |              4 |
| drop_unusable        |             11 |
| deflate_categoricals |              0 |
| encode_categoricals  |             55 |