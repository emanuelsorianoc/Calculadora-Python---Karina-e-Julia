import streamlit as st
st.title("Calculadora")
num1 = st.number_input("Insira o primeiro número: ")
num2 = st.number_input("Insira o segundo número: ")

operacao = st.selectbox("escolha uma operação: ", ["soma" ,"subtração" ,"divisão" ,"multiplicação"])
if st.button("calcular"):
    if operacao == "soma":
        resultado = num1 + num2
    elif operacao == "subtração":
        resultado = num1 - num2
    elif operacao == "divisão":
        resultado= num1 / num2
    else:
        resultado = num1 * num2

    st.write ("Resultado", resultado)