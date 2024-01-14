import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')  # lendo os dados

# título da visualização web
st.header('Visualização de dados de anúncio de vendas de carros')

hist_button = st.button('Criar histograma')  # criar um botão


if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


disp_button = st.button('Criar gráfico de dispersão')  # criar um botão

if disp_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, y="odometer", x="model_year")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
