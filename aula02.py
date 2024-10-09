# import o streamlit - baby step -1
import streamlit as st
#entre com um numero - baby step -2 
numero = st.number_input("Digite um número entre -10 ate 50:",step=1 )
#verificar se o número é positivo , negativo ou nulo  - baby step 3 
if numero > 0:
    st.write(f"Seu numero {numero} é positivo")
elif numero == 0:
    st.write(f"Seu numero {numero} é neutro")
else: 
    st.write(f"Seu numero {numero} é negativo")
