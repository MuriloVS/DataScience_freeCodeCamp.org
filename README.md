# DataScience - freeCodeCamp.org

Aplicativos para Data Sciente utilizando Streamlit - Tutorais do freeCodeCamp.org - https://youtu.be/JwSS70SZdyM


Para executar (localmente), dentro da pasta: streamlit run nomedoarquivo.py

## 1. Simple Stock Price App

Um aplicativo simples para mostrar, de maneira gráfica, a mudança diária no índide de uma ativo. Fiz algumas modificações para que fosse mostrado o índice IBOVESPA ao invés do valor da ação da Google.

## 2. Simple Bioinformatics DNA Counter

Conta os nucleotídeos no DNA. O usuário informa uma sequência de DNA e o web app gera a contagem dos nucleotídeos.
Foi feita uma pequena alteração na parte do código que lê a entrada da sequência genética, removendo/comentando texto/código desnecessários.


## 3. EDA Basketball

Utiliza web scrapping para pegar dados dos jogadores da NBA disponíveis no site https://www.basketball-reference.com/
Depois é possível gerar tabelas e mapas de calor dos jogadores de todos times, desde 1950 até 2021, com o uso de filtros.
Pequenas alterações foram feitas no código para resolver problemas do streamlit e também para deixar o código atualizado (pyplot).


## 4. EDA Football

Parecido com o app de basquete: utiliza web scrapping para pegar dados dos jogadores da NFL (https://www.pro-football-reference.com) e gerar tabelas com dados e mapa de calor. O foco é dado nas jardas percorridas pelos jogadores quando partem de trás da linha de scrimmage (rushing).
Código atualizado (pyplot).


## 5. EDA SP500 Stock Price

Utiliza web scrapping para pegar dados das 500 maiores empresas dos EUA (S&P 500). Inicialmente é recuperados os símbolos (stock symbol ticker) das empresas no SP500, assim como área de atuação - são os dados que podemos cruzar no webapp.
Foi necessário fazer um pequena adaptação no código inicial para resolver um pronblema de certificação.


