# Data Preparation Summary

Task:                   Classification
Data original shape:    504 samples × 22 features
Data final shape:       504 samples × 49 features
Target feature:         Dementia

Samples dropped due to NaN target: 0
Indicator variables added for continuous NaNs: 1

# Processing Times

| computation          |   runtime (ms) |
|:---------------------|---------------:|
| unify_nans           |             11 |
| convert_categoricals |              3 |
| inspect_target       |              7 |
| drop_target_nans     |              1 |
| encode_target        |              7 |
| drop_unusable        |              1 |
| deflate_categoricals |              0 |
| encode_categoricals  |             22 |