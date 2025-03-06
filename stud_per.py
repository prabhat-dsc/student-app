import pandas as pd 
import numpy as np 
import streamlit as st 
import pickle
from sklearn.preprocessing import StandardScaler,LabelEncoder
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://prabhatdsc487:prabha123@app-cluster.9joou.mongodb.net/?retryWrites=true&w=majority&appName=app-cluster"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db=client['student']
collection=db['student_pred']

def load_model():
    with open('student_lr_final_model.pkl','rb') as file:
        model,scaler,le=pickle.load(file)
    return model,scaler,le
def preprocess_input_data(data,scaler,le):
    data['Extracurricular Activities']=le.transform([data['Extracurricular Activities']])[0]
    df=pd.DataFrame(data,index=[0])
    df_transformed=scaler.transform(df)
    return df_transformed

def predict_data(data):
    model,scaler,le=load_model()
    processed_data=preprocess_input_data(data,scaler,le)
    prediction=model.predict(processed_data)
    return prediction

def main():
    st.title("Welcome to Ms. Prabhat Singh prediction App")
    st.write(" Enter the data  to get your performance Index !!")
    Study_Hours=st.number_input('Study_Hours',min_value=0,max_value=9,value=0)
    Previous_Scores=st.number_input('Previous_Scores',min_value=40,max_value=99,value=45)
    Extracurricular_Activities=st.selectbox('Extracurricular_Activities',['Yes','No'])
    Sleep_Hours=st.number_input('Sleep_Hours',min_value=4,max_value=9,value=4)
    Sample_Ques_Papers_Practiced=st.number_input('Sample_Ques_Papers_Practiced',min_value=0,max_value=9,value=1)
    if st.button("Predict your Score!!"):
        user_data={
            'Hours Studied':Study_Hours, 
            'Previous Scores':Previous_Scores, 
            'Extracurricular Activities':Extracurricular_Activities,
            'Sleep Hours':Sleep_Hours, 
            'Sample Question Papers Practiced':Sample_Ques_Papers_Practiced
        }
        prediction=  predict_data(user_data)  
        st.success(f'Your prediction result is:: {prediction}')
        user_data['prediction']=int(prediction)
        user_data['Extracurricular Activities']=int(user_data['Extracurricular Activities'])
  
        collection.insert_one(user_data)
        st.success(f'user data is inserted to DB')

if __name__=='__main__':
    main()
