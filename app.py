from numpy import append
import streamlit as st
import joblib





hide_streamlit_style = """
        <style>
        
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
html_temp = """
<body style="background-color:red;">
<div style="background-color:#1A4645 ;padding:10px">
<h2 style="color:white;text-align:center;">Predict Change in CGPA during Online Semesters</h2>
<p style="color:white;text-align:center;"> This model has been trained with data provided by private universiity students of Bangladesh. To contribute towards the dataset, take <a href="https://forms.gle/Hfz955LPyrP8EKNM6" target="_blank">this survey</a></p>
</div>
</body>
"""
st.markdown(html_temp, unsafe_allow_html=True)

Living_Area = st.radio("What would you describe your living area as?", ('Rural area', 'Urban area'))

Family = st.radio("Are you currently living with your family?", ('Yes', 'No'))

Devices=st.radio("How many devices do you have available for online classes?", ('1', '2', 'more than 2'))

Internet_type=st.radio("What type of internet connection do you have?", ('Broadband', 'Mobile Internet'))

Internet_stability =st.radio("How stable is your Internet connection?", ('0', '1', '2', '3', '4'))

Loadshedding= st.radio("How long are the usual hours for load shedding (power outage) in your area?", ('0 hours', '1-3 hours', '3-5 hours', 'more than 5 hours'))

Studied_more= st.radio("When did you spend more time studying?", ('Before Online classes started.', 'After Online classes started'))

CGPA_before= st.slider("What was your CGPA before online classes started?",0.0,4.0)

Submission_type= st.radio("AWhich one do you think is easier for you?", ('Submitting assignments online', 'Submitting assignments offline'))

Mental_health= st.radio("Do you think online education had any negative impact on your mental health?", ('Yes', 'No'))

Online_exam =st.radio("Rate your experience with online examinations", ('0', '1', '2', '3', '4'))

Online_class= st.radio("Rate your comfortability with online classes", ('0', '1', '2', '3', '4'))

Online_teacher =st.radio("Rate the quality of communication with your teacher during online sessions", ('0', '1', '2', '3', '4'))


choicelist=[]
if st.button('PREDICT'):
    if Living_Area == 'Rural area':
        choicelist.append(0)
    else:
        choicelist.append(1)
    if Family == 'Yes':
        choicelist.append(1)
    else:
        choicelist.append(0)
    if Devices == '1':
        choicelist.append(0)
    elif Devices == '2':
        choicelist.append(1)
    else:
        choicelist.append(2)
    if Internet_type == 'Broadband':
        choicelist.append(0)
    else:
        choicelist.append(1)
    choicelist.append(int(Internet_stability))
    if Loadshedding == '0 hours':
        choicelist.append(0)
    elif Loadshedding == '1-3 hours':
        choicelist.append(1)
    elif Loadshedding == '3-5 hours':
        choicelist.append(2)   
    else:
        choicelist.append(3)
    if Studied_more == 'Before Online classes started.':
        choicelist.append(1)
    else:
        choicelist.append(0)
    choicelist.append(CGPA_before)
    if Submission_type == 'Submitting assignments online':
        choicelist.append(1)
    else:
        choicelist.append(0)
    if Mental_health == 'Yes':
        choicelist.append(1)
    else:
        choicelist.append(0)
    choicelist.append(int(Online_exam))
    choicelist.append(int(Online_class))
    choicelist.append(int(Online_teacher))
    finalarray=(choicelist,)
    loaded_log_clf = joblib.load("Logistic_Regression_compressed.joblib")
    result= loaded_log_clf.predict(finalarray)[0]

    if result == 'Decreased':
        st.warning("Your CGPA might Decrease!")
    else:
        st.success("Your CGPA will not Decrease!")
