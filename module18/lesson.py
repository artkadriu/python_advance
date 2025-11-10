import pandas as pd
import streamlit as st


st.header("Display Data")

data = pd.DataFrame({
    'Name':['Blin','Enes','GHELLO'],
    'Age':[19,20,21],
    'City' : ['Prishtina', 'Ferizaj', 'Peja']
})

st.dataframe(data)