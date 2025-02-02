# Data Preparation Summary

Task:                   Classification
Data original shape:    1000 samples × 20 features
Data final shape:       1000 samples × 31 features
Target feature:         Dementia

Samples dropped due to NaN target: 0
Indicator variables added for continuous NaNs: 0

# Processing Times

| computation          |   runtime (ms) |
|:---------------------|---------------:|
| unify_nans           |             17 |
| convert_categoricals |              3 |
| inspect_target       |              3 |
| drop_target_nans     |              1 |
| encode_target        |              4 |
| drop_unusable        |             16 |
| deflate_categoricals |              0 |
| encode_categoricals  |             78 |