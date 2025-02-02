==============================================================================================================================================================================
                                                                           Destructive Data Changes                                                                           
==============================================================================================================================================================================
Removed Features
----------------

Constants
┄┄┄┄┄┄┄┄┄
Gender   Single value even if including NaNs

==============================================================================================================================================================================
                                                                        Feature Cardinality Inferences                                                                        
==============================================================================================================================================================================

Binary Features
---------------
APOE_ε4              Two unique non-Nan values
Depression_Status    Two unique non-Nan values
Diabetic             Two unique non-Nan values
Medication_History   Two unique non-Nan values
Sleep_Quality        Two unique non-Nan values
Dominant_Hand        Two unique non-Nan values
Family_History       Two unique non-Nan values

Categorical Features
--------------------
Physical_Activity           Data not interpretable as numeric
Nutrition_Diet              Data not interpretable as numeric
Education_Level             Data not interpretable as numeric
Chronic_Health_Conditions   Data not interpretable as numeric
Smoking_Status              Data not interpretable as numeric

Numeric Features
----------------

Ordinals
┄┄┄┄┄┄┄┄
HeartRate   Integers not starting at 0 or 1
Age         Integers not starting at 0 or 1

Continuous
┄┄┄┄┄┄┄┄┄┄
Weight             All values are not integers and convert to float
BloodOxygenLevel   All values are not integers and convert to float
AlcoholLevel       All values are not integers and convert to float
BodyTemperature    All values are not integers and convert to float

