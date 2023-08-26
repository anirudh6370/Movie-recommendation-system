import streamlit as st
import pandas as pd
import pickle
import difflib
import requests
from config import TMDB_API_KEY

with open('movies-dict.pkl', 'rb') as file:
    loaded_dict = pickle.load(file)
    
with open('cosine_similarity.pkl', 'rb') as file:
    similarity = pickle.load(file)

movie = pd.DataFrame(loaded_dict)

API_KEY = TMDB_API_KEY
def fetch_movie_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        poster_path = data.get('poster_path')
        if poster_path:
            poster_url = f'https://image.tmdb.org/t/p/w500{poster_path}'
            return poster_url
    return None

def recomend(movie_name):
    close_match=difflib.get_close_matches(movie_name,movie.original_title.tolist())
    #it gives all close matches of that particular movie. it is helpfull in case of certain spelling mistake of the user.
    rec_names=[]
    rec_posters=[]
    if len(close_match) != 0:
        index=movie[movie["original_title"]==close_match[0]].index[0]#we are taking the first element into consideration because it is very much close to that word than others. 
        distance = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
        for i in distance[1:6]:#we are taking 5 close movies into consideration other than itself
            rec_names.append(movie.iloc[i[0]].original_title)
            rec_posters.append(fetch_movie_poster(movie.iloc[i[0]].id))
        return rec_names,rec_posters

st.title('MOVIE RECOMMENDATION SYSTEM')
selected_movie = st.selectbox('Enter Movie Name',movie['original_title'].values)
if st.button('Recommend'):
    names,posters = recomend(selected_movie)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.image(posters[0], caption=names[0])
    
    with col2:
        st.image(posters[1], caption=names[1])
    
    with col3:
        st.image(posters[2], caption=names[2])

    with col4:
        st.image(posters[3], caption=names[3])
    
    with col5:
        st.image(posters[4], caption=names[4])
