# Data Preparation Summary

Task:                   Classification
Data original shape:    1000 samples × 23 features
Data final shape:       1000 samples × 39 features
Target feature:         Dementia

Samples dropped due to NaN target: 0
Indicator variables added for continuous NaNs: 1

# Processing Times

| computation          |   runtime (ms) |
|:---------------------|---------------:|
| unify_nans           |              8 |
| convert_categoricals |              1 |
| inspect_target       |              2 |
| drop_target_nans     |              1 |
| encode_target        |              2 |
| drop_unusable        |              9 |
| deflate_categoricals |              0 |
| encode_categoricals  |             42 |