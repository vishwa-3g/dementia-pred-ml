# Data Preparation Summary

Task:                   Classification
Data original shape:    496 samples × 20 features
Data final shape:       496 samples × 30 features
Target feature:         Dementia

Samples dropped due to NaN target: 0
Indicator variables added for continuous NaNs: 0

# Processing Times

| computation          |   runtime (ms) |
|:---------------------|---------------:|
| unify_nans           |              8 |
| convert_categoricals |              2 |
| inspect_target       |              1 |
| drop_target_nans     |              1 |
| encode_target        |              2 |
| drop_unusable        |             11 |
| deflate_categoricals |              0 |
| encode_categoricals  |             47 |