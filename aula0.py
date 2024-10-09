# aqui eu importo o streamlit 

import streamlit as st 

"""
Estamos iniciando o streamlit
ele nos ajuda no projeto final 
em sua instação vem incluida o pandas e outras libs .
"""
idade = st.number_input("Digite sua idade :", min_value=14, max_value=120)  # aqui e um renge , ja valida a entrada 
if idade >= 18:
    #uso obrigatorio de identaçao 
    st.write(f"Alô Mundo - você é maior de idade:{idade} anos")
else:
    st.write("Alô Mundo_ você é menor de idade:{idade} anos")

