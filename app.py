import pickle
import streamlit as st

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

# Streamlit app layout
st.header('Movie Recommender System')

# Load movies and similarity data
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)

# Show recommendations
if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)

    cols = st.columns(5)
    for col, name in zip(cols, recommended_movie_names):
        with col:
            st.text(name)

