import pandas as pd # type: ignore
import numpy as np # type: ignore
import streamlit as st # type: ignore
import pickle
from sklearn.preprocessing import StandardScaler,LabelEncoder # type: ignore


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
    st.title("Welcome to Ms. Lucky Singh prediction App")
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

if __name__=='__main__':
    main()
