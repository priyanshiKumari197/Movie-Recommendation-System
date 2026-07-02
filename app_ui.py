import streamlit as st
import pickle

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ==========================
# Load Data
# ==========================
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# ==========================
# Recommendation Function
# ==========================
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations


# ==========================
# UI
# ==========================

st.title("🎬 Movie Recommendation System")
st.write("Get movie recommendations based on your favorite movie using Content-Based Filtering.")

selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movies["title"].values
)

if st.button("Recommend Movies"):

    recommendations = recommend(selected_movie)

    st.subheader("🍿 Top 5 Recommended Movies")

    for i, movie in enumerate(recommendations, start=1):
        st.success(f"{i}. {movie}")