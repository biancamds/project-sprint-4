import pandas as pd
import plotly.express as px
import streamlit as st


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

    #inserir título na página
    st.markdown('##### Dados gerais')

    # exibir a tabela com o intervalo de fabricantes geral (inclui fabricantes com menos de 1000 anúncios)
    # deixar o texto 'Tabela geral' em negrito
    st.markdown('**Tabela**', unsafe_allow_html=True)
    st.write(data_adjusted.iloc[:, :11])

    # criar gráfico
    # definir paleta de cores para o gráfico
    pastel_colors = px.colors.qualitative.Plotly[:len(
        data_counts['type'].unique())]

    # criar o gráfico de barras empilhadas da quantidade de tipos por fabricante
    fig = px.bar(data_counts, x='manufacturer', y='count', color='type',
                 title='Contagem geral de tipos por fabricante',
                 color_discrete_sequence=pastel_colors)  # utilizar paleta de cores estabelecida

    # exibir o gráfico de barras no Streamlit
    st.plotly_chart(fig)

    # criar o gráfico histograma da condição do veículo por ano do modelo
    fig = px.histogram(data_adjusted, x='model_year', color='condition',
                       title='Histograma de condição vs. ano do modelo',
                       color_discrete_sequence=pastel_colors)
    
    # exibir o gráfico histograma no Streamlit
    st.plotly_chart(fig)

    # criar o gráfico de dispersão do preço do veículo por ano do modelo separado pelas categorias de transmissão
    fig = px.scatter(data_adjusted, x='model_year', y='price', color='transmission',
                       title='Gráfico de dispersão do preço do veículo vs. ano do modelo separado por categorias de transmissão',
                       color_discrete_sequence=pastel_colors)
    
    # exibir o gráfico de dispersão no Streamlit
    st.plotly_chart(fig)

else:

    #inserir título na página
    st.markdown('##### Dados filtrados')

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
    st.markdown('**Tabela**', unsafe_allow_html=True)
    st.write(data_filter.iloc[:, :11])

    # definir paleta de cores para o gráfico
    pastel_colors = px.colors.qualitative.Plotly[:len(
        data_counts_filter['type'].unique())]

    # criar o gráfico de barras empilhadas da quantidade de tipos por fabricante
    fig = px.bar(data_counts_filter, x='manufacturer', y='count', color='type',
                 title='Contagem filtrada de tipos por fabricante',
                 color_discrete_sequence=pastel_colors)  # utilizar paleta de cores estabelecida

    # exibir o gráfico de barras no Streamlit
    st.plotly_chart(fig)

    # criar o gráfico histograma da condição do veículo por ano do modelo
    fig = px.histogram(data_filter, x='model_year', color='condition',
                       title='Histograma de condição vs. ano do modelo',
                       color_discrete_sequence=pastel_colors)
    
    # exibir o gráfico histograma no Streamlit
    st.plotly_chart(fig)

    # criar o gráfico de dispersão do preço do veículo por ano do modelo separado pelas categorias de transmissão
    fig = px.scatter(data_filter, x='model_year', y='price', color='transmission',
                       title='Gráfico de dispersão do preço do veículo vs. ano do modelo separado por categorias de transmissão',
                       color_discrete_sequence=pastel_colors)
    
    # exibir o gráfico de dispersão no Streamlit
    st.plotly_chart(fig)