from xml.parsers.expat import model
import pandas as pd
import numpy as np
import streamlit as st
import joblib
import sklearn

modelo = joblib.load('titanic_model.pkl')


st.title("Tela de predição para sobreviventes TITANIC")
genre = st.radio(
    "Selecione o Genero",
    ["Masculino", "Feminino"],
    index=None,
)
if genre == "Masculino":
    sexo =1
else:
    sexo =0

option = st.selectbox(
    "Selecione a classe contratatda",
    ("A", "B", "C"),
)

st.write("A classe selecionada foi:", option)
if option == "A":
    classe = 1
elif option == "B":
    classe = 2
else:
    classe = 3

idade = st.number_input(label="Idade: ",min_value=0, max_value=100)

cônjuges  = st.number_input(label="Digite o número de cônjuges correspondente:",min_value=0, max_value=10)

embarque = st.selectbox(
    "Selecione a Local de Embarque:",
    ("A", "C", "Q"),
)
st.write("O Local de embarque selecionado foi:", embarque)
if option == "A":
    embarque = 0
elif option == "B":
    embarque = 1
else:
    embarque = 2

parentes  = int(st.number_input('Número de parentes abordo: ', min_value=0, max_value=6))
valor = float(st.number_input('Digite o valor pago pelo bilete: '))


if st.button(label="Verificar", key=None, help=None, on_click=None, args=None, kwargs=None,type="secondary", icon=None, disabled=False, use_container_width=False):

    dados = np.array([classe,sexo,idade,cônjuges,parentes,valor, embarque]).reshape(1,-1)
    print(type(modelo.predict(dados)))
    sobreviveu = modelo.predict(dados)
    valor22 = modelo.predict_proba(dados)
  
    if modelo.predict(dados) == 0:
        valor22 = modelo.predict_proba(dados)
        sobr = 'Não'
        v = (valor22[0][0]  * 100)
        st.text("Não sobreviveu!")
        st.metric(label='A probabilidade de não sobreviver é: ',value=v, border=True)
     
       
    elif modelo.predict(dados)==1:
        valor22 = modelo.predict_proba(dados)
        sobr = 'Sim'
        v = (valor22[0][1] * 100)
        st.text("Sobreviveu! ")
        st.metric(label='A probabilidade de sobreviver é de: ',value=str(round(v,2))+'%', border=True)