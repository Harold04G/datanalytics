import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Mi primera publicación Streamlit")
st.header("Introducción")
st.write("Esta es mi primera publicación en Streamlit.")
st.subheader("Cambios en la publicación")


st.write("Este es un gráfico de barras simple.")
fig = px.bar(
    x=["A", "B", "C"],
    y=[1, 2, 3],
    title="Gráfico de barras",
)
st.plotly_chart(fig)
date = st.date_input("Pick a date")