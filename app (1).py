

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#Loading the saved models


diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_disease_model.sav','rb'))


#Sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction and Health bot'],
                           icons = ['activity','heart','person'],
                           default_index = 0)
    
    
#Diabetes Prediction Page
if(selected == 'Diabetes Prediction'):
    
    #Page title
    st.title('Diabetes Prediction using ML')
    
    Glucose = st.number_input('Glucose Level')
    Pregnancies =  st.number_input('Number of Pregnancies')
    BloodPressure = st.number_input('Blood Pressure value')
    SkinThickness = st.number_input('Skin Thickness value')
    Insulin = st.number_input('Insulin Level')
    BMI =  st.number_input('BMI value')
    DiabetesPedigreeFunction =  st.number_input('Diabetes Pedigree Function value')
    Age =  st.number_input('Age of the Person')
    
    
    #Code for prediction
    diab_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is Not Diabetic'
            
            
    st.success(diab_diagnosis)
    
    
    
            
#Heart Disease Prediction Page
if(selected == 'Heart Disease Prediction'):
    
    #Page title
    st.title('Heart Disease Prediction using ML')
    
    age = st.number_input('Age of the Person')
    sex = st.number_input('Sex of the Person')
    cp = st.number_input('Chest pain types')
    trestbps = st.number_input('Resting Blood Pressure')
    chol = st.number_input('Serum Cholestoral in mg/dl')
    fbs = st.number_input('Fasting blood sugar > 120 mg/dl')
    restecg = st.number_input('Resting Electrocardiographic results')
    thalach = st.number_input('Maximum Heart Rate achieved')
    exang = st.number_input('Exercise Induced Angina')
    oldpeak = st.number_input('ST depression induced by exercise')
    slope = st.number_input('Slope of the peak exercise ST segment')
    ca = st.number_input('Mjor vessels colored by flourosopy')
    thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    
    #Code for prediction
    heart_diagnosis = ''
    
    #Creating a button for prediction
    
    if st.button('Heart Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0]==1):
            heart_diagnosis = 'The person is suffering from Heart disease'
            
        else:
            heart_diagnosis = 'The person is Not suffering from Heart disease'
            
            
    st.success(heart_diagnosis)
    
    
    

    
#Parkinsons Prediction Page
if(selected == 'Parkinsons Prediction and Health bot'):
    
    #Page title
    st.title('Parkinsons Prediction using ML')
    

    fo =  st.number_input('MDVP:Fo(Hz)')
    fhi = st.number_input('MDVP:Fhi(Hz)')
    flo =  st.number_input('MDVP:Flo(Hz)')
    Jitter_percent =  st.number_input('MDVP:Jitter(%)')
    Jitter_Abs =  st.number_input('MDVP:Jitter(Abs)')
    RAP =  st.number_input('MDVP:RAP')
    PPQ =  st.number_input('MDVP:PPQ')
    DDP =  st.number_input('Jitter:DDP')
    Shimmer =  st.number_input('MDVP:Shimmer')
    Shimmer_dB =  st.number_input('MDVP:Shimmer(dB)')
    APQ3 =  st.number_input('Shimmer:APQ3')
    APQ5 =  st.number_input('Shimmer:APQ5')
    APQ =  st.number_input('MDVP:APQ')
    DDA =  st.number_input('Shimmer:DDA')
    NHR =  st.number_input('NHR')
    HNR =  st.number_input('HNR')
    RPDE =  st.number_input('RPDE')
    DFA =  st.number_input('DFA')
    spread1 =  st.number_input('spread1')
    spread2 =  st.number_input('spread2')
    D2 =  st.number_input('D2')
    PPE =  st.number_input('PPE')
        
        
    #Code for prediction
    parkinsons_diagnosis = ''
        
    #Creating a button for prediction
        
    if st.button('Parkinsons Test Result'):
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            
            if (parkinsons_prediction[0]==1):
                parkinsons_diagnosis = 'The person is suffering from Parkinsons disease'
                
            else:
                parkinsons_diagnosis = 'The person is Not suffering from Parkinsons disease'
    st.success(parkinsons_diagnosis)
                
    st.markdown("""
    <iframe src='https://webchat.botframework.com/embed/healthcarebot-zoksepr?s=Fzx1oELAJ1o.CXxCbwpIsHv5U_3Ddj6gD0zwxbCTX_Reh8nmYq2h8pU' 
            style='min-width:400px; width: 100%; min-height: 500px;' 
            frameborder='0' 
            scrolling='no'>
    </iframe>
""", unsafe_allow_html=True)
                

        
        