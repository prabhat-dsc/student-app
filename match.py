import streamlit as st 
import pickle
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url = "mongodb+srv://prabhatdsc487:prabha123@app-cluster.9joou.mongodb.net/?retryWrites=true&w=majority&appName=app-cluster"
# Create a new client and connect to the server
client = MongoClient(url, server_api=ServerApi('1'))
db=client['cricket']
collection=db['match_poll']


def main():
    st.title("Welcome to ICC Champion Trophy  prediction")
    st.write(" Select your Opinion who will win India Vs Newzealand!!")
    Name=st.text_input(" Your Name Please")
    City=st.text_input('Your City Location')
    st.write(" Select  India Vs Newzealand !!")
    Poll=st.selectbox('Poll',['India','Newzealand'])

    if st.button("SUBMIT"):
        user_data={
            'Name':Name,
            'City':City,
            'Poll':Poll
        }

        st.success(f'Thank you !!')

        collection.insert_one(user_data)

if __name__=='__main__':
    main()