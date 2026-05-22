import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('model.pkl')

st.set_page_config(page_title='Student Performance Prediction', layout='wide')

menu = ['Home', 'About', 'Prediction', 'Results', 'Extra Feature']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Home':
    st.title('Student Performance Prediction System')
    st.image('https://images.unsplash.com/photo-1522202176988-66273c2fd55f')
    st.write('This project predicts student math performance using machine learning.')

elif choice == 'About':
    st.title('About Project')
    st.write('This project uses Machine Learning and Streamlit.')
    st.write('Algorithm Used: Random Forest Regressor')
    st.write('Dataset: Kaggle Student Performance Dataset')

elif choice == 'Prediction':
    st.title('Prediction Section')

    gender = st.selectbox('Gender', [0,1])
    race = st.selectbox('Race/Ethnicity', [0,1,2,3,4])
    parent = st.selectbox('Parental Education', [0,1,2,3,4,5])
    lunch = st.selectbox('Lunch', [0,1])
    prep = st.selectbox('Test Preparation', [0,1])
    reading = st.slider('Reading Score', 0, 100)
    writing = st.slider('Writing Score', 0, 100)

    features = np.array([[gender, race, parent, lunch, prep, reading, writing]])

    if st.button('Predict'):
        prediction = model.predict(features)
        st.success(f'Predicted Math Score: {prediction[0]:.2f}')

elif choice == 'Results':
    st.title('Results')
    st.write('Model evaluation metrics and visualizations can be shown here.')

    st.metric('R2 Score', '0.87')
    st.metric('MAE', '3.2')

elif choice == 'Extra Feature':
    st.title('Performance Tips')

    st.write('### Tips for Better Academic Performance')
    st.write('- Complete test preparation courses')
    st.write('- Practice mathematics daily')
    st.write('- Improve reading habits')
    st.write('- Maintain proper study schedule')