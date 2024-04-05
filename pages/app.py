
import streamlit as st
import pickle
import pandas as pd
import requests

# Load movies data
movies = pickle.load(open("movies_list.pkl", 'rb'))
cosine_sim = pickle.load(open("cosine_sim2.pkl", 'rb'))

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=a5024058dd6379b74e7cb0fd67ac962c".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.header("CineCircle: The Social Movie Network ")

indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Function to get recommendations for a given movie
def get_recommendations(movie, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[movie]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommend_movies = []
    recommend_poster = []

    # Get the top 10 most similar movies
    for i in sim_scores[1:11]:
        movie_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))

    return recommend_movies, recommend_poster

# Main function to recommend movies for each genre
def recommend_movies_for_genres(genres):
    for genre in genres:
        st.header(f"Movies Recommendations for {genre}")

        count = 0
        num_columns = 10
        columns = st.columns(num_columns)
        
        

        for index, movie_genres in movies['genres'].iteritems():
            if count < num_columns and genre in movie_genres:
                with columns[count]:
                    st.image(fetch_poster(movies['id'][index]))
                    st.text(movies['title'][index])
                count += 1

# Usage
selected_genres = ["adventure", "fantasy", "action"]
recommend_movies_for_genres(selected_genres)
