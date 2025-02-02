#TO RUN THE PYTHON FILES

python3 MLD_W_Pres.py



#WITH ALL COLUMNS PRESENT

# FOR MAIN DATASET
python3 df-analyze.py --spreadsheet /Users/gagandeepsingh/Documents/MLD_Tab1/df-analyze/dementia_patients_health_data.csv --target Dementia --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --feat-select filter embed wrap --redudant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --test-val-size 0.4 --outdir ./results         

#FOR MALE DATASET
python3 df-analyze.py --spreadsheet /Users/gagandeepsingh/Documents/MLD_Tab1/df-analyze/male.csv --target Dementia --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --feat-select filter embed wrap --redudant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --test-val-size 0.4 --outdir ./results         

#FOR FEMALE DATASET
python3 df-analyze.py --spreadsheet /Users/gagandeepsingh/Documents/MLD_Tab1/df-analyze/female.csv --target Dementia --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --feat-select filter embed wrap --redudant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --test-val-size 0.4 --outdir ./results  


#WITH REMOVED COLUMNS

#FOR MAIN DATASET
python3 df-analyze.py --spreadsheet /Users/gagandeepsingh/Documents/MLD_Tab1/df-analyze/Dementia_wp_Pres.csv --target Dementia --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --feat-select filter embed wrap --redudant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --test-val-size 0.4 --outdir ./results

#FOR MALE DATASET
python3 df-analyze.py --spreadsheet /Users/gagandeepsingh/Documents/MLD_Tab1/df-analyze/Male_drop.csv --target Dementia --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --feat-select filter embed wrap --redudant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --test-val-size 0.4 --outdir ./results  

#FOR FEMALE DATASET
python3 df-analyze.py --spreadsheet /Users/gagandeepsingh/Documents/MLD_Tab1/df-analyze/Female_drop.csv --target Dementia --mode classify --classifiers knn lgbm rf lr sgd dummy gandalf --feat-select filter embed wrap --redudant-wrapper-selection --embed-select lgbm linear --wrapper-select step-up --wrapper-model linear --norm robust --nan median --filter-method assoc pred --filter-assoc-cont-classify mut_info --filter-assoc-cat-classify mut_info --filter-pred-classify acc --htune-trials 50 --htune-cls-metric acc --test-val-size 0.4 --outdir ./results  