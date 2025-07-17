import streamlit as st
import pandas as pd
import json

# Load data
with open('data/books.json') as f:
    books = json.load(f)

df = pd.DataFrame(books)

st.title("📚 Book Search App")
st.write("Data scraped from [Books to Scrape](https://books.toscrape.com/)")

search_query = st.text_input("Cari Judul Buku")

if search_query:
    results = df[df['title'].str.contains(search_query, case=False)]
else:
    results = df

st.write(f"Hasil: {len(results)} buku ditemukan")
st.dataframe(results)
