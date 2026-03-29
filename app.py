import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="ReadSphere", layout="wide")

# Load data
popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_score = pickle.load(open('similarity_score.pkl','rb'))

st.title("📚 ReadSphere - Book Recommender")

# ===============================
# 🔥 Section 1: Popular Books
# ===============================
st.header("🔥 Popular Books")

cols = st.columns(4)

for i in range(8):  # show top 8 books
    with cols[i % 4]:
        st.image(popular_df['Image-URL-M'][i])
        st.write(popular_df['Book-Title'][i])
        st.write(popular_df['Book-Author'][i])
        st.write("⭐", popular_df['avg_rating'][i])

# ===============================
# 🔍 Section 2: Recommendation
# ===============================
st.header("🔍 Get Book Recommendations")

user_input = st.selectbox("Type or select a book", pt.index.values)

if st.button("Recommend"):
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_score[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:5]

    st.subheader("📖 Recommended Books")

    cols = st.columns(4)

    for i, item in enumerate(similar_items):
        temp_df = books[books['Book-Title'] == pt.index[item[0]]]

        with cols[i]:
            st.image(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values[0])
            st.write(temp_df.drop_duplicates('Book-Title')['Book-Title'].values[0])
            st.write(temp_df.drop_duplicates('Book-Title')['Book-Author'].values[0])
