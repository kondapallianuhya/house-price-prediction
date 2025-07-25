import streamlit as st
import joblib
import numpy as np

model = joblib.load("archive/model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app uses machine learning for predicting house price with given features of the house ,for using app you can enter inputs from this UI and then use predict button.")

st.divider()

bedrooms = st.number_input("Number of bedrooms",min_value =0, value = 0)
bathrooms= st.number_input("Number of bathrooms",min_value =0, value = 0)
livingarea=st.number_input("Living area",min_value=0, value = 2000)
condition=st.number_input("Condition",min_value=0, value=3)
numberofschools=st.number_input("Number of schools nearby",min_value=0, value = 0)

st.divider()

X = [[bedrooms,bathrooms,livingarea,condition,numberofschools]]

predictbutton = st.button("Predict")

if predictbutton:
    
    st.balloons()
    
    X_array = np.array(X)
    
    prediction = model.predict(X_array)[0]
    
    st.write(f"Price prediction is {prediction:,.2f}")
else:
    st.write("Please use predict button after entering values")
        




 






#Order of X'number of bedrooms', 'number of bathrooms', 'living area',
       #'condition of the house', 'Number of schools nearby']
