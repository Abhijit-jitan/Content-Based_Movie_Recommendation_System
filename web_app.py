import streamlit as st
import pandas as pd
import numpy as np
import Backend.recommend

## Main Heading
st.title("----- Movie Recommendation System -----")
st.subheader(" Recommend Me Movie ")
## Loading Data
data=pd.read_csv(r"C:\Users\jitan\Referances\content_based movie recommendation system\movie_data.csv")
movies_name=data["title"].values

## Recommendation System
select=st.selectbox("Select A Movie Name : ",movies_name)
if st.button("Recommend Me"):
    st.subheader("Recommended Movies")
    recommend_movies=recommend.recommend(select)
    for movie_id,movies_name in recommend_movies.items():
        st.write("======> {}".format((movies_name)))


# movies=recommend("Pirates of the Caribbean: On Stranger Tides")
# # movies=recommend("Furious 7")
# # for movie in movies:
# #     print("ID:{} - {} ;Similarity'{}'".format(movie[0],movie[1],movie[2]))

