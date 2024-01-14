import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import re


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


# scatter_button = st.button('Criar gráfico de dispersão')  # criar um botão

# if scatter_button:  # se o botão for clicado
#     # escrever uma mensagem
#     st.write(
#         'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

#     # criar um gráfico de dispersão
#     fig = px.scatter(car_data, y="odometer", x="model_year")

#     # exibir um gráfico Plotly interativo
#     st.plotly_chart(fig, use_container_width=True)

# # criar um botão
# build_histogram = st.checkbox('Criar um histograma - teste')

# if build_histogram:  # se o botão 'build_histogram' for clicado
#     # escrever uma mensagem
#     st.write(
#         'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

#     # criar um histograma
#     fig = px.histogram(car_data, x="odometer")

#     # exibir um gráfico Plotly interativo
#     st.plotly_chart(fig, use_container_width=True)

# criar um botão
build_scatter = st.checkbox('Criar um gráfico de dispersão - teste')

if build_scatter:  # se o botão 'build_scatter' for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de dispersão
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


fig.add_trace(
    go.Table(
        header=dict(
            values=["teste", "model_year", "model",
                    "condition", "cylinders", "fuel",
                    "odometer", "transmission", "type",
                    "paint_color", "is_4wd"],
            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[car_data[k].tolist() for k in car_data.columns[1:]],
            align="left")
    ),
    row=1, col=1
)

fig.update_layout(
    height=800,
    showlegend=False,
    title_text="Bitcoin mining stats for 180 days",
)

fig.show()
