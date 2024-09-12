import streamlit as st
import requests
import pandas as pd
import streamlit_lottie as st_lottie
from streamlit_option_menu import option_menu
import joblib
import numpy as np
import PIL as Image
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
page_title="Stroke Prediction",page_icon=':gem:',initial_sidebar_state='collapsed'


)

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

model=joblib.load(open("stroke",'rb'))

def predict(gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status):
    features=np.array([gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]).reshape(1,-1)
    prediction = model.predict(features)
    return prediction


with st.sidebar:
    choose = option_menu(None, ["Home", "Graphs", "About","Contact"],
                        icons = ["house", "kanban", "book","person lines fill"],
                        menu_icon="app-indicator",default_index=0,
    styles = {
        "container": {"padding": "5!important","background-color":"#fafafa"},
        "icon": {"color": "#E0E0EF","font-size":"25px"},
        "nav-link": {"text-align":"left","font-size":"16px","margin":"0px","--hover-color": "#eee"},
        "nav-link:selected": {"background-color": "#02ab21"},
    })

if choose =='Home':
    st.write("# stroke Potability")
    st.subheader("Enter the values to predict the potability of stroke")
    gender= st.radio("select your gender :",('male','female'))
    gender_encoder=1 if gender =='male' else 0
    age= st.number_input("Enter your age",min_value=0.0,step=1.0)
    hypertension= st.radio("do you have hypertension ",('Yes','No'))
    hypertension_encoder=1 if hypertension =='Yes' else 0
    heart_disease= st.radio("do you have heart_disease",('Yes','No'))
    heart_disease_encoder=1 if heart_disease =='Yes' else 0
    ever_married= st.radio("are you married",('Yes','No'))
    ever_married_encoder=1 if ever_married =='Yes' else 0
    work_type= st.radio("Work Type",('Self employed','Private','Govt_job'))
    if work_type =='Self employed': work_type_encoder=0
    elif work_type =='Private': work_type_encoder=1
    else : work_type_encoder=2
    Residence_type= st.radio("Residence type",('Urban','Rural'))
    Residence_type_encoder=1 if Residence_type =='Urban' else 0
    avg_glucose_level= st.number_input("Enter avg glucose level",min_value=0.0,step=1.0)
    bmi= st.number_input("Enter bmi",min_value=0.0,step=0.2)
    smoking_status= st.radio("Enter the status of smoking",('smokes','never-smoked','formerly-smoked','unknown'))
    if smoking_status =='smokes': smoking_status_encoder=0
    elif smoking_status =='never-smoked': smoking_status_encoder=1
    elif smoking_status =='formerly-smoked': smoking_status_encoder=2
    else : smoking_status=3
    # predict the potability of stroke
    sample=predict(gender_encoder,age,hypertension_encoder,heart_disease_encoder,ever_married_encoder,work_type_encoder,Residence_type_encoder,avg_glucose_level,bmi,smoking_status_encoder)
    if st.button("Predict"):
        if sample == 1:
            st.warning("# you have stroke")
        elif sample == 0:
            st.success("# you don't have stroke")
            st.balloons()
        
elif choose == "Graphs":
    st.write("# srtoke Potability Graphs")
    st.image("images/download.png")
    st.image("images/download (1).png")
    st.image("images/download (2).png")
    st.image("images/download (3).png")
    st.image("images/download (4).png")
elif choose == "About":
    st.write("# About stroke Potability")
    st.write("stroke potability refers to the quality of stroke in terms of its chemical, physical, and biological characteristics in relation to the health of humans and animals. This is a very important aspect of water quality since it determines the safety of water for human consumption and other uses.")
    st.write("The potability of stroke is determined by the presence of various chemical substances in stroke. These substances include pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity. The presence of these substances in water can affect its potability.")
    st.write("The potability of stroke can be determined using various methods such as chemical analysis, physical testing, and biological testing. These methods are used to determine the presence of harmful substances in water and to ensure that water is safe for human consumption.")
elif choose == "Contact":
    st.write("# Contact Us")
data = pd.read_csv(r"C:\Users\AHMED\Documents\python\healthcare-dataset-stroke-data (1).csv")
df=pd.DataFrame(data)