import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
import re


# função para ler e armazenar em cache o arquivo CSV
read_and_cache_csv = st.cache_data(pd.read_csv)

# carregar os dados usando a função cacheada
data = read_and_cache_csv('vehicles.csv')

# selecionar o intervalo de colunas
data_selected = data.iloc[:, :11]

# criar coluna específica com nome do fabricante
# criar uma cópia para evitar alterações no DataFrame original
data_adjusted = data_selected.copy()
data_adjusted['manufacturer'] = data_selected['model'].str.split().str[0]

# novo DataFrame com dados gerais selecionados nas colunas 'manufacturer' e 'type'
data_counts = pd.DataFrame({
    'manufacturer': data_adjusted['manufacturer'],
    'type': data_adjusted['type']
})

# dados gerais agrupados e contados por tipo e por fabricante
data_counts = data_counts.groupby(
    ['manufacturer', 'type']).size().reset_index(name='count')

# título da visualização web
st.header('Visualização de dados de anúncio de vendas de carros')

# criar uma caixa de seleção
table_checkbox = st.checkbox('Incluir fabricantes com menos de 1000 anúncios')

if table_checkbox:  # se a caixa for selecionada

    # exibir a tabela com o intervalo de fabricantes geral (inclui fabricantes com menos de 1000 anúncios)
    # deixar o texto 'Tabela geral' em negrito
    st.markdown('**Tabela geral**', unsafe_allow_html=True)
    st.write(data_selected)

    # criar gráfico
    # definir paleta de cores para o gráfico
    pastel_colors = px.colors.qualitative.Plotly[:len(
        data_counts['type'].unique())]

    # criar o gráfico de barras empilhadas da quantidade de tipos por fabricante
    fig = px.bar(data_counts, x="manufacturer", y="count", color="type",
                 title="Contagem geral de tipos por fabricante",
                 color_discrete_sequence=pastel_colors)  # utilizar paleta de cores estabelecida

    # exibir o gráfico no Streamlit
    st.plotly_chart(fig)

else:
    # filtrar tabela
    # agrupar os dados por fabricante e calcular a soma das contagens para cada fabricante
    manufacturer_grouped = data_counts.groupby('manufacturer')[
        'count'].sum()

    # filtrar os fabricantes cuja soma das contagens é superior a 1000
    manufacturer_above_1000 = manufacturer_grouped[manufacturer_grouped > 1000]

    # obter a lista dos fabricantes cuja soma das contagens é superior a 1000
    list_manufacturer_above_1000 = manufacturer_above_1000.index.tolist()

    # filtrar os dados originais mantendo apenas as linhas correspondentes aos fabricantes acima de 1000
    data_filter = data_adjusted[data_adjusted['manufacturer'].isin(
        list_manufacturer_above_1000)].reset_index(drop=True)

    # novo DataFrame com dados filtrados nas colunas 'manufacturer' e 'type'
    data_counts_filter = pd.DataFrame({
        'manufacturer': data_filter['manufacturer'],
        'type': data_filter['type']
    })

    # dados filtrados agrupados e contados por tipo e por fabricante
    data_counts_filter = data_counts_filter.groupby(
        ['manufacturer', 'type']).size().reset_index(name='count')

    # criar tabela filtrada
    # Deixa o texto 'Tabela geral' em negrito
    st.markdown('**Tabela filtrada**', unsafe_allow_html=True)
    st.write(data_filter.iloc[:, :11])

    # definir paleta de cores para o gráfico
    pastel_colors = px.colors.qualitative.Plotly[:len(
        data_counts_filter['type'].unique())]

    # criar o gráfico de barras empilhadas da quantidade de tipos por fabricante
    fig = px.bar(data_counts_filter, x="manufacturer", y="count", color="type",
                 title="Contagem filtrada de tipos por fabricante",
                 color_discrete_sequence=pastel_colors)  # utilizar paleta de cores estabelecida

    # exibir o gráfico no Streamlit
    st.plotly_chart(fig)


# # hist_button = st.button('Criar histograma')  # criar um botão


# # if hist_button:  # se o botão for clicado
# #     # escrever uma mensagem
# #     st.write(
# #         'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

# #     # criar um histograma
# #     fig = px.histogram(car_data, x="odometer")

# #     # exibir um gráfico Plotly interativo
# #     st.plotly_chart(fig, use_container_width=True)


# # scatter_button = st.button('Criar gráfico de dispersão')  # criar um botão

# # if scatter_button:  # se o botão for clicado
# #     # escrever uma mensagem
# #     st.write(
# #         'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

# #     # criar um gráfico de dispersão
# #     fig = px.scatter(car_data, y="odometer", x="model_year")

# #     # exibir um gráfico Plotly interativo
# #     st.plotly_chart(fig, use_container_width=True)

# # # criar um botão
# # build_histogram = st.checkbox('Criar um histograma - teste')

# # if build_histogram:  # se o botão 'build_histogram' for clicado
# #     # escrever uma mensagem
# #     st.write(
# #         'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

# #     # criar um histograma
# #     fig = px.histogram(car_data, x="odometer")

# #     # exibir um gráfico Plotly interativo
# #     st.plotly_chcheckboxart(fig, use_container_width=True)

# # # criar um botão
# # build_scatter = st.('Criar um gráfico de dispersão - teste')

# # if build_scatter:  # se o botão 'build_scatter' for clicado
# #     # escrever uma mensagem
# #     st.write(
# #         'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

# #     # criar um gráfico de dispersão
# #     fig = px.scatter(car_data, y="price", x="model_year")

# #     # exibir um gráfico Plotly interativo
# #     st.plotly_chart(fig, use_container_width=True)
