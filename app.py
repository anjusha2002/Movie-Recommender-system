import streamlit as st #pip install streamlit
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['name'] == movie].index.values[0]  # to get the index of particular movie
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id =i[0]

        #fetch poster from API

        recommended_movies.append(movies['name'].iloc[i[0]])
    return recommended_movies



st.title('Movie Recommender System')
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity =pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox('How would u like to be contacted?',movies['name'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
