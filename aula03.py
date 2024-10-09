import streamlit as st 
import pandas as pd 
st.title("Carregue o seu dataSet")

upload = st.file_uploader("escolha o arquivo ", type="csv")

if upload is not None:
    df = pd.read_csv(upload)
    st.dataframe(df)