import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title('Healthcare Prediction -Patient stay in Hospital')
# load dataset
#df = pd.read_csv("train.csv")

# show the entire dataframe
#st.write(df)

# f-string
#st.subheader('Hospital Stay')
#stay_count = df['Stay'].value_counts()
#st.text(f'Hospital Stay frequency = {stay_count.values[1]/sum(stay_count):.2%}')

# simple plotting
#fig, ax = plt.subplots(1, 2, figsize=(15, 5))
#stay_count.plot.bar(ax=ax[0])
#df['Age'].plot.hist(ax=ax[1])
#st.pyplot(fig)

# markdown
st.subheader('Making Prediction')
st.markdown('**Please provide patient information**:')  # you can use markdown like this

# load models
tree_clf = joblib.load('2clf-best.pickle')

# get inputs
hospital_code = int(st.selectbox('Hospital Code:', [ 8, 2, 10, 26, 23, 32,  1, 22, 16,  9, 6, 29, 12,  3, 21, 28, 27, 19,  5, 14, 13, 31, 24, 17, 25, 15, 11, 30, 18,  4,  7, 20]))
hospital_type_code = st.selectbox('Hospital type code:', ['c', 'e', 'b', 'a', 'f', 'd', 'g'])
city_code_hospital = int(st.selectbox('City code hospital:', [ 3,  5,  1,  2,  6,  9, 10,  4, 11,  7, 13]))
hospital_region_code = st.selectbox('Hospital region code:', ['Z', 'X', 'Y'])
available_extra_rooms = st.selectbox('Available Extra Rooms in Hospital:', [ 3,  2,  1,  4,  6,  5,  7,  8,  9, 10, 12,  0, 11, 20, 14, 21, 13, 24])
department = st.selectbox('Department:', ['radiotherapy', 'anesthesia', 'gynecology', 'TB & Chest disease', 'surgery'])
Ward_Type = st.selectbox('Ward type:', ['R', 'S', 'Q', 'P', 'T', 'U'])
ward_facility_code = st.selectbox('Ward facility code:', ['F', 'E', 'D', 'B', 'A' ,'C'])
bed_grade = float(st.selectbox('Bed grade:', [ 2.,  3.,  4.,  1.]))
patientid = int(st.number_input('Patientid:', 0, 50000, 0))
city_code_patient = float(st.selectbox('City code patient:', [ 7.,  8.,  2.,  5.,  6.,  3.,  4.,  1.,  9., 14., 25., 15., 12., 10., 28., 24., 23., 20., 11., 13., 21., 18., 16., 26., 27., 22., 19., 31., 34., 32., 30., 29., 37., 33., 35., 36., 38.]))
type_of_admission = st.selectbox('Type of Admission:', ['Emergency', 'Trauma', 'Urgent'])
severity_of_illness = st.selectbox('Severity of Illness:', ['Extreme', 'Moderate', 'Minor'])
visitors_with_patient = int(st.number_input('Visitors with Patient:', 0, 10, 0))
age = st.selectbox('Age:', ['51-60', '71-80', '31-40', '41-50', '81-90', '61-70', '21-30', '11-20', '0-10', '91-100'])
admission_deposit = float(st.number_input('Admission_Deposit:', 0, 100000, 0))


# this is how to dynamically change text
prediction_state = st.markdown('calculating...')

patient = pd.DataFrame(
    {
        'Hospital_code': [hospital_code],
        'Hospital_type_code': [hospital_type_code],
        'City_Code_Hospital': [city_code_hospital],
        'Hospital_region_code': [hospital_region_code],
        'Available Extra Rooms in Hospital': [available_extra_rooms],
        'Department': [department],
        'Ward_Type': [Ward_Type],
        'Ward_Facility_Code': [ward_facility_code],
        'Bed Grade': [bed_grade],
        'patientid': [patientid],
        'City_Code_Patient': [city_code_patient],
        'Type of Admission': [type_of_admission],
        'Severity of Illness': [severity_of_illness],
        'Visitors with Patient': [visitors_with_patient],
        'Age': [age],
        'Admission_Deposit': [admission_deposit]
    }
)
y_pred = tree_clf.predict(patient)

msg = 'This patient is predicted to stay: '+ y_pred

prediction_state.markdown(msg)


