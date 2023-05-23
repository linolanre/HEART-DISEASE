import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')
from sklearn.linear_model import LogisticRegression
import joblib

model = joblib.load(open('LinReg.pkl', 'rb'))

st.title('HEART RATE TEST')
st.subheader('Built By Gomycode scions')

st.image('pngwing.com.png')

st.write('Pls register your name for the record')
username = st.text_input('Enter Your Name')


if st.button('Submit'):
    st.success(f"Welcome {username}. Pls use according to usage guidelines")

picture = st.sidebar.camera_input('Position your face to the webcam')
if picture:
    st.image(picture)



input_type = st.sidebar.selectbox('Choose your preferred input type', ['Number Input', 'Slider'])

if input_type == 'Number Input':
    biking = st.sidebar.number_input('Biking', 1.1, 75.0, 38.0)
    smoking = st.sidebar.number_input('Smoking', 0.5, 30.0, 15.4)

else:
    biking = st.sidebar.slider('Biking', 1.1, 75.0, 38.0)
    smoking = st.sidebar.slider('Smoking', 0.5, 30.0, 15.4)


input_values = {'biking': biking, 'smoking': smoking}
input_df = pd.DataFrame(input_values, index=[0])

st.write('This is your inputted Data')
st.table(input_df)

prediction = model.predict(input_df)

if st.button('Predict'):
    input_df['Heart Rate'] = prediction
    st.table(input_df)
    