# Data Preparation Summary

Task:                   Classification
Data original shape:    504 samples × 20 features
Data final shape:       504 samples × 30 features
Target feature:         Dementia

Samples dropped due to NaN target: 0
Indicator variables added for continuous NaNs: 0

# Processing Times

| computation          |   runtime (ms) |
|:---------------------|---------------:|
| unify_nans           |              5 |
| convert_categoricals |              1 |
| inspect_target       |              1 |
| drop_target_nans     |              1 |
| encode_target        |              3 |
| drop_unusable        |              7 |
| deflate_categoricals |              0 |
| encode_categoricals  |             38 |