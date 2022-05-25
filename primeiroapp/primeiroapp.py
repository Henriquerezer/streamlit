import streamlit as st


st.markdown('Olá a todos este é meu primeiro aplicativo streamlit, decorrente do curso de **DEPLOY PARA DATA APPS**, utilizei a biblioteca streamlit a qual deve ser instada em sua maquina, minha recomendação é que a instalação seja feita pelo **anaconda prompt**.')
st.markdown('O Google colab não suporta o streamlit, então por isso estou utilizando o anaconda, para a edição do código foi utilizado o ** Sublime Text**, o qual é compatível com diversas linguagens, inclusive **Python**.')
st.markdown('Em um primeiro momento deve ser realizada a instalação da biblioteca streamlit no anaconda prompt, conforme abaixo!')
st.code('pip install streamlit')
st.markdown('precisamos criar um arquivo **.py** no Sublime Text, ou por qualquer outra IDE de sua preferência!')
st.markdown('Após isso deve ser aberto o arquivo **.py** no próprio anaconda prompt, conforme código abaixo! **Lembrando que no prompt devemos procurar a o local em que o arquivo está no computador**')
st.code('C:\ Users\ Henrique>cd documents')
st.code('C:\ Users\ Henrique\ Documents>cd web app')
st.code('C:\ Users\ Henrique\ Documents\ web app>cd primeiro')
st.code('C:\ Users\ Henrique\ Documents\ web app\ primeiro>streamlit run primeiroapp.py')
st.markdown('Utilizando o código abaixo, estaremos abrindo o arquivo utilizando streamlit, o arquivo será aberto em seu browser.')
st.code('streamlit run primeiroapp.py')

st.markdown('###**Abaixo segue alguns testes feitos, afim de buscar a familiarização com a biblioteca!**')

st.title('Meu primeiro aplicativo streamlit!')

st.markdown('# Titulo')
st.markdown('## Titulo')
st.markdown('### Titulo')
st.markdown('*Titulo*')
st.markdown('**Titulo**')

st.markdown('Emojis do markdown: :smiley: :poop: :heart_eyes:')

st.write('Entrada padrão de texto')

st.text('Texto com aquela fonte quadrada')

st.code('import pandas as pd')

st.latex('\int_a^bf(x)dx = F(b) - F(a)')

st.sidebar.title('Meu primeiro aplicativo streamlit!')
st.sidebar.latex('\int_a^bf(x)dx = F(b) - F(a)')
st.sidebar.title('Barra Lateral')

n = st.slider('Entre com um número', 10, 70, 20, 2)

st.title(f'O quadrado de {n} é {n**2}')

nome = st.text_input('Digite o eu nome!')

botao = st.button('Clique aqui para finalizar: ')

if botao:
	st.info(f'**{nome.upper()}**, parabéns! Você concluiu sua primeira aula de streamlit')
	st.balloons()