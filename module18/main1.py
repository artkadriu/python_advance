import pandas as pd
import streamlit as st
import plotly.express as px


books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("best selling book analyses")
st.write("this is an app showing dataset")

st.subheader("Summery.statustics")
total_books = books_df.shape[0]
unique_titles = books_df ['Name'].nunique()
average_rating = books_df['User rating'].mean()
average_price = books_df['Price'].mean()

