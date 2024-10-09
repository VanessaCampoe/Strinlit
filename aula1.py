import streamlit as st 
import requests
import pandas as pd
import json


st.title("DASHBOARD DE VENDAS:shopping_trolley:")
#st.button("click me")
url = "https://labdados.com/produtos?regiao=norte&ano=2022"
response = requests.get(url)
# json
#dicionario 
# Dataframe


df = pd.DataFrame.from_dict(response.json())
if st.button("todos"):
    st.balloons()
    st.metric("Receita",df["preço"].sum())
    st.metric("Quantidade de vendas (linhas)",df.shape[0])
    st.metric("Quantidade de vendas (colunas)",df.shape[1])
    st.dataframe(df)
    st.snow()
else:
    st.write("clique no botão todos")



