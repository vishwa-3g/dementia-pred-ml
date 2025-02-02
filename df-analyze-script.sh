# Student Name - Gagandeep Singh(Student id- 202303876)
# Student Name - Vishwashree Karhadkar(Student id- 202307962)

For Main Dataset

python3 df-analyze.py --spreadsheet /Users/gagandeepsingh/Documents/MLD/df-analyze/dementia_patients_health_data.csv --target Dementia --mode classify --classifiers knn lgbm rf lr sgd dummy --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --test-val-metric mae --test-val-size 0.4 --outdir ./results

For Male Dataset

python3 df-analyze.py --spreadsheet /Users/gagandeepsingh/Documents/MLD/df-analyze/male.csv --target Dementia --mode classify --classifiers knn lgbm rf lr sgd dummy --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --test-val-metric mae --test-val-size 0.4 --outdir ./results

For Female Dataset
python3 df-analyze.py --spreadsheet /Users/gagandeepsingh/Documents/MLD/df-analyze/female.csv --target Dementia --mode classify --classifiers knn lgbm rf lr sgd dummy --feat-select filter embed wrap --redundant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --test-val-metric mae --test-val-size 0.4 --outdir ./results
