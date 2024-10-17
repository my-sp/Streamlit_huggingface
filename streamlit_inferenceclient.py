import streamlit as st
import requests
from huggingface_hub import InferenceClient
st.title("Streamlit with Hugging Face API")
def get_models():
    response = requests.get("https://huggingface.co/api/models")
    return response.json() 
models = get_models()
print(models)
model_names = [model['modelId'] for model in models]
#select a model
selected_model = st.selectbox("Select the model:", model_names)
api_token = "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"
client = InferenceClient(model=selected_model,token=api_token)
user_input = st.text_input("Enter text:")

if user_input:
    response = client.text_generation(user_input)
    st.write(response)
elif user_input == "":
    st.write("Please enter some text to generate a response.")

