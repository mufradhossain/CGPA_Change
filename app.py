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
<p style="color:white;text-align:center;"> This model has been trained with data provided by private universiites of Bangladesh. To contribute towards the dataset, take <a href="https://forms.gle/Hfz955LPyrP8EKNM6" target="_blank">this survey</a></p>
</div>
</body>
"""
st.markdown(html_temp, unsafe_allow_html=True)

Internet_stability =st.radio("How stable is your Internet connection?", ('0', '1', '2', '3', '4'))

Loadshedding= st.radio("How long are the usual hours for load shedding (power outage) in your area?", ('0 hours', '1-3 hours', '3-5 hours', 'more than 5 hours'))

CGPA_before= st.slider("What was your CGPA before online classes started?",0.0,4.0)

Online_exam =st.radio("Rate your experience with online examinations", ('0', '1', '2', '3', '4'))

Online_class= st.radio("Rate your comfortability with online classes", ('0', '1', '2', '3', '4'))

Online_teacher =st.radio("Rate the quality of communication with your teacher during online sessions", ('0', '1', '2', '3', '4'))


choicelist=[]
if st.button('PREDICT'):
    choicelist.append(int(Internet_stability))
    if Loadshedding == '0 hours':
        choicelist.append(0)
    elif Loadshedding == '1-3 hours':
        choicelist.append(1)
    elif Loadshedding == '3-5 hours':
        choicelist.append(2)   
    else:
        choicelist.append(3)
    choicelist.append(CGPA_before)
    choicelist.append(int(Online_exam))
    choicelist.append(int(Online_class))
    choicelist.append(int(Online_teacher))
    finalarray=(choicelist,)
    loaded_rf = joblib.load("random_forest_compressed.joblib")
    result= loaded_rf.predict(finalarray)[0]

    if result == 'Decreased ( হ্রাস পেয়েছে )':
        st.warning("Your CGPA might not increase!")
    else:
        st.success("Your CGPA might increase!")
