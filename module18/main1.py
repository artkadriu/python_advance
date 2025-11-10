import pandas as pd
import streamlit as st
import plotly.express as px
import os


file_path = os.path.join(os.path.dirname(__file__), 'bestsellers_with_categories_2022_03_27.csv')
books_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("best selling book analyses")
st.write("this is an app showing dataset")

st.subheader("Summery.statistics")
total_books = books_df.shape[0]
unique_titles = books_df ['Name'].nunique()
average_rating = books_df['User rating'].mean()
average_price = books_df['Price'].mean()

col1, col2,col3,col4 = st.columns(4)
col1.metric('Total Books', total_books)
col2.metric('Unique Books', unique_titles)
col3.metric('Average Books', f'{average_rating:.2f})')
col4.metric('Average Price', f"${average_price:.2f}")

st.subheader("Dataset Preview")
st.write(books_df.head())

col1,col2 = st.columns(2)

with col1:
    st.subheader("top 10 book titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)
    with col2:
        st.subheader("top 10 book titles")
        top_titles = books_df['Name'].value_counts().head(10)
        st.bar_chart(top_authors)


    st.subheader("genre distribution")
    fig = px.pie(books_df, names="Genre", title="Most liked genre (2009-2022)", color= 'Genre',
                 color_discrete_sequence=px.colors.sequential.Plasma)

    st.plotly_chart(fig)

st.subheader("Number of fiction vs non fiction books over the years")
size = books_df.groupby(['Year','Genre']).size().reset_index(name='Counts')
fig= px.bar(size, x='Year', y= 'counts', color='genre', title="Number of fiction vs non fiction",
            color_discrete_sequence=px.colors.sequential.Plasma, barmode='group')

st.plotly_chart(fig)

st.subheader("Top 15 Authors by counts of books published (2009-2022)")
top_authors = books_df ['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author','Count']

fig = px.bar(top_authors, x='count', y='Author', orientation='h', title='Top 15 Aut counts of books published' ,
labels= {'Count': 'Count of books published','Author':'Author'}, color='count',
color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Filter Data by Genre")
genre_filter = st.selectbox("Select Genre", books_df['Genre'].unique())
filtered_df = books_df[books_df['Genre'] == genre_filter]

st.write(filtered_df)
