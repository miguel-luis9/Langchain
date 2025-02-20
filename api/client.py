import requests
import streamlit as st

def get_deep_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
                           json={'input':{'topic': input_textDeep}})
    return response.json()['output']['content']

def get_llama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke",
                           json={'input':{'topic': input_text}})
    return response.json()['output']

st.title('Langchain Demo using Llama and DeepSeek APIs')
input_text=st.text_input("Write an essay on")
input_textDeep=st.text_input("Write a poem on")

if input_text:
    st.write(get_llama_response(input_text))

if input_textDeep:
    st.write(get_deep_response(input_textDeep))