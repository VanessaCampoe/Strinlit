
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

def formatar_numero(valor):
        if valor >= 1000000:
            return f" {valor/1000000:.2f} milhões"
        elif valor >= 1000:
            return f" {valor/1000:.2f} mil"
        else:
            return f" {valor:.2f}" 

st.title("Dashboard de Vendas:shopping_trolley:")

url = "https://labdados.com/produtos"
response = requests.get(url)
df = pd.DataFrame.from_dict(response.json())
# balões
st.balloons()
# valor total
#st.metric('Receita',formatar_numero(df['Preço'].sum()))
st.metric('Receita',formatar_numero(1000000))
# a quantidade de vendas
st.metric('Qtde Vendas',formatar_numero(df.shape[0]))
# a quantidade de variáveis
st.metric('Qtde de variáveis',df.shape[1])
st.dataframe(df)
st.snow()