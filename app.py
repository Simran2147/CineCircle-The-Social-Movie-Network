import streamlit as st
import pickle
import pandas as pd
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
cosine_sim = pickle.load(open("cosine_sim2.pkl", 'rb'))
movies_list=movies['title'].values
selectvalue=st.selectbox("Select movie from dropdown", movies_list)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

st.header("Movie Recommender System")



indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()

def get_recommendations(movie, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[movie]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    recommend_movies = []
    recommend_poster = []
    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    movies_id= [i[0] for i in sim_scores]
    recommend_movies.append(movies['title'].iloc[movie_indices])
    recommend_poster.append(fetch_poster(movies['id'].iloc[movies_id]))
    # Return the top 10 most similar movies
    return recommend_movies,recommend_poster



if st.button("Show Recommend"):
    movie_name, movie_poster = get_recommendations(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])