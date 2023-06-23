


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)



#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(T, TM, Tm, SLP, H, VV, V, VM ,CO2,CH4	):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[T, TM, Tm, SLP, H, VV, V, VM,CO2,CH4]])
    print(prediction)
    return prediction



def main():
    st.title("AIR QUALITY PREDICTION")
    html_temp = """
    <div style="background-color:blue;padding:10px">
    <h2 style="color:white;text-align:center;">STREAMLIT AIR QUALITY WEB APP </h2>
    </div>
    <div>
    <h3>air quality level above 151 means = Good Air quality</h3>
    <h4>air quality level below 151 means = bad Air quality</h4>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    T = st.text_input("T	","Type Here")
    TM = st.text_input("TM","Type Here")
    Tm = st.text_input("Tm","Type Here")
    SLP= st.text_input("SLP","Type Here")
    H = st.text_input("H","Type Here")
    VV = st.text_input("VV","Type Here")
    V= st.text_input("V","Type Here")
    VM	 = st.text_input("VM	","Type Here")
    CO2	 = st.text_input("CO2	","Type Here")
    CH4	 = st.text_input("CH4	","Type Here")
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(T, TM, Tm, SLP, H, VV, V, VM,CO2,CH4)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    