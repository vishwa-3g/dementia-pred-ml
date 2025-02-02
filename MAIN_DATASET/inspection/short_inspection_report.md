===========================================================================================================================================================
                                                                  Destructive Data Changes                                                                 
===========================================================================================================================================================

Cardinality Coercions
---------------------
Cognitive_Test_Scores   Coerced to ordinal due to no decimal, feature name or undersampled levels

===========================================================================================================================================================
                                                               Feature Cardinality Inferences                                                              
===========================================================================================================================================================

Binary Features
---------------
Medication_History   Two unique non-Nan values
Dominant_Hand        Two unique non-Nan values
Family_History       Two unique non-Nan values
Diabetic             Two unique non-Nan values
APOE_ε4              Two unique non-Nan values
Gender               Two unique non-Nan values
Depression_Status    Two unique non-Nan values
Sleep_Quality        Two unique non-Nan values

Categorical Features
--------------------
Smoking_Status              Data not interpretable as numeric
Nutrition_Diet              Data not interpretable as numeric
Prescription                Data not interpretable as numeric
Education_Level             Data not interpretable as numeric
Physical_Activity           Data not interpretable as numeric
Chronic_Health_Conditions   Data not interpretable as numeric

Numeric Features
----------------

Ordinals
┄┄┄┄┄┄┄┄
HeartRate               Integers not starting at 0 or 1
Age                     Integers not starting at 0 or 1
Cognitive_Test_Scores   Coerced to ordinal due to no decimal, feature name or undersampled levels

Continuous
┄┄┄┄┄┄┄┄┄┄
Weight             All values are not integers and convert to float
BodyTemperature    All values are not integers and convert to float
Dosage_in_mg       All values are not integers and convert to float
BloodOxygenLevel   All values are not integers and convert to float
AlcoholLevel       All values are not integers and convert to float

