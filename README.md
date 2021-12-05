# DataScience - freeCodeCamp.org

Aplicativos para Data Sciente utilizando Streamlit - Tutorais do freeCodeCamp.org - https://youtu.be/JwSS70SZdyM

## 1. Simple Stock Price App

Um aplicativo simples para mostrar, de maneira gráfica, a mudança diária no índide de uma ativo. Fiz algumas modificações para que fosse mostrado o índice IBOVESPA ao invés do valor da ação da Google.

Para executar (localmente): streamlit run myapp.py

## 2. Simple Bioinformatics DNA Counter

Conta os nucleotídeos no DNA. O usuário informa uma sequência de DNA e o web app gera a contagem dos nucleotídeos.
Foi feita uma pequena alteração na parte do código que lê a entrada da sequência genética, removendo/comentando texto/código desnecessários.

Para executar (localmente): streamlit run dnaapp.py


## 3. EDA Basketbal

Utiliza web scrapping para pegar dados dos jogadores da NBA disponíveis no site https://www.basketball-reference.com/
Depois é possível gerar tabelas e mapas de calor dos jogadores de todos times, desde 1950 até 2021, com o uso de filtros.
Pequenas alterações foram feitas no código para resolver problemas do streamlit e também para deixar o código atualizado (pyplot).

Para executar (localmente): streamlit run basketball_app.py