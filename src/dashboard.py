import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('dados/processado/musicas_sentimentos.csv')
fig = px.scatter(df, x='year', y='sentiment', hover_data=['title', 'album'], title='Sentimentos das Músicas de Bob Marley ao Longo dos Anos')

st.title('Reggae Insights: Biblioteca Musical Interativa de Bob Marley')
st.plotly_chart(fig)
st.dataframe(df)
