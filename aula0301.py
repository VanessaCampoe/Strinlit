import streamlit as st
# 1 crie um algoritimo que descubra um numero secreto !


# 2 criar o numero secreto 

numero_secreto = 7
# 3 titulo na aplicação 
st.title('jogodo Numero Secreto')

# 4 dar uma mensagem de boas vindas 

st.write("Boas vindas ao jogo do número secreto ")
# 5 receber o chute do ussuario 
chute = st.number_input("Escolha um numero de 1 a 10 ", min_value =1,max_value=10,step=1)


# 6 verificar o chute com o numero secreto 
if st.button("Verificar"):
    if chute == numero_secreto:

# 7 mostrar uma mensagem personalizada 
        st.balloons()

        st.success(f"Isso ai! Você acertou o número secreto: {numero_secreto}")
        st.snow()
    else:
        st.error(f"Infelizmente você errou! O codigo era: {numero_secreto}!Tente novamente!")


