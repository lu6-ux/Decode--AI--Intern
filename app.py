import streamlit as st
import pandas as pd


# Movie dataset
movies = {
    "Movie": [
        "Avengers",
        "Batman",
        "Titanic",
        "Frozen",
        "Spider-Man"
    ],

    "Genre": [
        "Action",
        "Action",
        "Romance",
        "Animation",
        "Action"
    ],

    "Mood": [
        "Exciting",
        "Dark",
        "Emotional",
        "Happy",
        "Exciting"
    ]
}


df = pd.DataFrame(movies)


st.title("🎬 AI Movie Recommendation System")

st.write("Tell us your preferences")


# User inputs

genre = st.selectbox(
    "Choose your favorite genre",
    df["Genre"].unique()
)


mood = st.selectbox(
    "Choose your mood",
    df["Mood"].unique()
)



# Recommendation logic

if st.button("Recommend"):

    result = df[
        (df["Genre"] == genre) &
        (df["Mood"] == mood)
    ]


    if len(result) > 0:

        st.success("Recommended Movies:")

        for movie in result["Movie"]:
            st.write("⭐", movie)

    else:

        st.warning(
            "No exact match found. Try another preference."
        )