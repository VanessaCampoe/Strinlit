import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import pandas as std
import json

def muda_valor(valor):
        if valor >= 1000000:
            return f" {valor/1000000:.1f} milhões"
        elif valor >= 1000:
            return f" {valor/1000:.1f} mil"
        else:
            return f" {valor:.2f}" 

st.title("Dashboard de Vendas:shopping_trolley: ")
url="https://labdados.com/produtos"
response= requests.get(url)

# json > convertido para dicionário > Convertido para databframe
df = pd.DataFrame.from_dict(response.json())
if st.button("todos"):
    st.balloons()         
    st.metric("Receita R$:",muda_valor(df['Preço'].sum()))
    st.metric("Quantidade de vendas (linhas)",muda_valor(df.shape[0]))
    st.metric("Quantidade de variaveis (colunas)",df.shape[1])   
    
    st.dataframe(df)
    st.snow()