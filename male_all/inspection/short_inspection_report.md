==========================================================================================================================================================================
                                                                         Destructive Data Changes                                                                         
==========================================================================================================================================================================
Removed Features
----------------

Constants
┄┄┄┄┄┄┄┄┄
Gender   Single value even if including NaNs

Cardinality Coercions
---------------------
Cognitive_Test_Scores   Coerced to ordinal due to no decimal, feature name or undersampled levels

==========================================================================================================================================================================
                                                                      Feature Cardinality Inferences                                                                      
==========================================================================================================================================================================

Binary Features
---------------
Diabetic             Two unique non-Nan values
Sleep_Quality        Two unique non-Nan values
Family_History       Two unique non-Nan values
APOE_ε4              Two unique non-Nan values
Medication_History   Two unique non-Nan values
Dominant_Hand        Two unique non-Nan values
Depression_Status    Two unique non-Nan values

Categorical Features
--------------------
Physical_Activity           Data not interpretable as numeric
Education_Level             Data not interpretable as numeric
Prescription                Data not interpretable as numeric
Smoking_Status              Data not interpretable as numeric
Nutrition_Diet              Data not interpretable as numeric
Chronic_Health_Conditions   Data not interpretable as numeric

Numeric Features
----------------

Ordinals
┄┄┄┄┄┄┄┄
Age                     Integers not starting at 0 or 1
HeartRate               Integers not starting at 0 or 1
Cognitive_Test_Scores   Coerced to ordinal due to no decimal, feature name or undersampled levels

Continuous
┄┄┄┄┄┄┄┄┄┄
BloodOxygenLevel   All values are not integers and convert to float
Dosage_in_mg       All values are not integers and convert to float
BodyTemperature    All values are not integers and convert to float
Weight             All values are not integers and convert to float
AlcoholLevel       All values are not integers and convert to float

