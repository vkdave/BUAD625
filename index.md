# healthcareml
This repo demonstrates how to predict the length of stay of a patient to observe if one can improve the efficiency of the healthcare management in a hospital.  The aim is to accurately predict the Length of Stay for each patient on case by case basis so that the Hospitals can use this information for optimal resource allocation and better functioning. 

To predict the length of stay of an individual, we will be using a supervised classification model as the stay of an individual is given in a range of days, or discrete outputs. We will use the training data that includes the individual’s length of stay to train our model, then use k-fold validation to predict the stay of an individual from the test fold. 

Tested with Python 3.5.6

The data used in this repo is: &nbsp; [Health Care Analytics - 2](https://www.kaggle.com/vetrirah/av-healthcare2)

## Data
- `test.csv`: This file contains the raw data with the observations surrounding different features that were collected as part of health camps. <br />
    - `case_id`:	Case_ID registered in Hospital <br />
    - `Hospital_code`:	Unique code for the Hospital <br />
    - `Hospital_type_code`:	Unique code for the type of Hospital <br />
    - `City_Code_Hospital`:	City Code of the Hospital <br />
    - `Hospital_region_code`:	Region Code of the Hospital <br />
    - `Available Extra Rooms in Hospital`:	Number of Extra rooms available in the Hospital <br />
    - `Department`:	Department overlooking the case <br />
    - `Ward_Type`:	Code for the Ward type <br />
    - `Ward_Facility_Code`:	Code for the Ward Facility <br />
    - `Bed Grade`:	Condition of Bed in the Ward <br />
    - `patientid`:	Unique Patient Id <br />
    - `City_Code_Patient`:	City Code for the patient <br />
    - `Type of Admission`:	Admission Type registered by the Hospital <br />
    - `Severity of Illness`:	Severity of the illness recorded at the time of admission <br />
    - `Visitors with Patient`:	Number of Visitors with the patient <br />
    - `Age`:	Age of the patient <br />
    - `Admission_Deposit`:	Deposit at the Admission Time <br />
    - `Stay`:	Stay Days by the patient <br />

## Exploratory Data Analysis

- Much of the data does not seem to be correlated with the patient's length of stay and is generally evenly distributed across all features. For example, the severity of an individual’s admission to the hospital does not appear to correlate with their length of stay.
- By looking through the different region codes and hospital codes we also found that individuals (patientid) had several different entries for their stay in the hospital, and
occasionally moved to different hospitals for each stay.
- There was a data formatting issue in the stay field that converted a text value (’11-20’) was switched to 20-Nov. Two of the attributes ‘Bed Grade’ and ‘Patient_City_Code’ attributes have null values.

### *Key Findings*

- Being a medical/patient dataset the gender feature which is an important one is not one of the attributes captured in the dataset.
- Although we were restricted by our dataset not including the gender of the patient, we found that most individuals are most likely women as most of patients were going into the
gynecology department for treatment. as there was around 80% of the patients are admitted to the Gynecology department.
- It appears like that dataset is heavily engineered as some feature combinations do not align with the medical domain observations. ex. length of hospital stay does not correlate with severity of admission.
- The baseline accuracy for the patient was identified to be 27.5% based on the max percentage of the patient stay across the Stay categories

## Preprocessing

- All categorical fields were encoded to numerical values for better visualization of the data spread mathematically.
- Created SciKitLearn pre-processing stages for numerical features and applied SimpleImputer (mean, median) for missing data and StandardScalar for scaling the different values to a standard numerical range to avoid any feature bias
- Created SciKitLearn pre-processing states for cateogrical features and applied SimpleImputer (most frequent) for missing data and OneHotEncoder to ensure the categorical fields are included in the model.
- Created features like 'Number of patient visits' and 'Proximity Ranking for the hospital' based on the number of visits to a hospital by the patient.

### *Key Findings*
- Though the engineered features ideally would have an impact in the real-life scenarios, due to the nature of the dataset (being highly engineered) these features when included in the model evaluation didn't yield the better prediction for the stay

## Model Selection

- Considering this to be a classification problem, Accuracy metric was identified as the driving factor among model selection.
- The basic models like Decision Tree and Random Forest were considered for this prediction. With the pre-processing of the data and no hyperparameter tuning, the models started yielding predictions that are better than the baseline prediction. 
- To further verify with other models, Logistic Regression model with different hyperparameter settings was used for the prediction. However, none of the Logistic Regression model results were better than the results from either of the decision tree or random forest results.
- With the solution now narrowed down to Decision tree and Random Forest models, the associated hyperparameters for each of the models were tuned to find the model that gave highest accuracy percentage.
    - Decision Tree: (tree depth, quality of the split (gini, entropy) 
    - Random Forest: Number of decision trees and quality of the split (gini, entropy)
- Based on the highest accuracy among the models, the Decision Tree model was selected as the final model for predicting the outcome surrounding the 'Stay' feature.

## Model Deployment

- Once the model was tuned and trained, it was exported to a pickle file. Along with the pickle file a basic python app leveraging streamlit library is deployed to Heroku to allow for capturing the testing data that the model will be predicting on in real-time. Below is the link to the application:

https://team1-healthcareml.herokuapp.com/

## Files

- `EDA_FeatureEngineering.ipnyb`: EDA and Feature Engineering Source
- `ModelTuning_and_Selection.ipynb`: Data pre-procesing and Model comparision and evaluation
- `Final Model Deployment.ipnyb`: Final model implemenation
- `healthcareapp.py`: streamlit app file
- `Procfile` and `setup.sh`: heroku deployment files

## Team Members

- Greg Neal
- Hemant Kini
- Lucas Freire
- Siva Kodali
- Vivek Dave

## Credits 
 
Mentor/Guide: &nbsp; Harry Wang &nbsp; (http://harrywang.me/about)

## References

- www.kaggle.com
- https://datahack.analyticsvidhya.com
- https://github.com
