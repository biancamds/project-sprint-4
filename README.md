
# Visualização de Dados de Anúncios de Vendas de Carros

Este projeto utiliza o Streamlit e o Plotly Express para criar visualizações interativas de dados de anúncios de vendas de carros a partir de um arquivo CSV. Ele inclui gráficos de barras empilhadas, histogramas e gráficos de dispersão para analisar diferentes aspectos dos dados.


## Como Executar (Pré-requisitos)

Certifique-se de ter o Python instalado em seu ambiente. Em seguida, instale as bibliotecas necessárias usando:

_pip install pandas plotly streamlit_

Execute o aplicativo Streamlit com o seguinte comando:

_streamlit run seu_script.py_

O aplicativo será executado no navegador e você poderá interagir com as visualizações.

Você também pode acessar o aplicativo web através do URL: *https://projeto-web-abq8.onrender.com/*


## Conteúdo do Código

O código está organizado da seguinte forma:

* app.py: Contém o código principal do aplicativo Streamlit.
* vehicles.csv: O arquivo CSV contendo os dados de anúncios de vendas de carros.

O código realiza as seguintes operações:

* Carrega os dados do CSV utilizando a função criada read_and_cache_csv para armazenamento em cache.
* Realiza algumas manipulações nos dados, como a criação de uma coluna 'manufacturer'.
* Cria visualizações interativas com diferentes opções de filtragem.


## Funcionalidades do Aplicativo

* A tabela e os gráficos são interativos, permitindo a seleção de fabricantes com base em diferentes critérios.
* Os gráficos incluem informações visuais de condição vs. ano do modelo por meio de histograma e um gráfico de dispersão de preço vs. ano do modelo por categorias de transmissão.
* Os dados são separados em duas possibilidades de visualização: incluindo fabricantes com menos de 1000 anúncios (dados gerais) e não incluindo fabricantes com menos de 1000 anúncios (dados filtrados). É possível alterar entre as duas formas através da seleção da caixa de seleção "Incluir fabricantes com menos de 1000 anúncios" logo abaixo do título do projeto no início da página.