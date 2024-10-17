import streamlit as st
import requests
st.title("Streamlit with Hugging Face API")
def get_models():
    response = requests.get("https://huggingface.co/api/models")
    return response.json() 
models = get_models()
model_names = [model['modelId'] for model in models]

# User selects a model
selected_model = st.selectbox("Select the model:", model_names)
API_URL = f"https://api-inference.huggingface.co/models/{selected_model}"
headers = {"Authorization": f"Bearer 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"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
input_text = st.text_input("Enter text:")

if st.button("Generate"):
    data = query({"inputs": input_text})
    st.write(data[0]['generated_text']) 
