import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from Backend.util_functions import recommend
from Backend.util_functions import utils


## Page title & icon
st.set_page_config(page_title="Movie Recommender", page_icon='🤖')


## Main Heading

# Header Image In Center Aligned
image = Image.open(r'D:\Projects\Content-Based_Movie_Recommendation_System-main\3658607.jpg')
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(image, use_column_width=True)

# Header In Center Aligned
st.markdown("<h1 style='text-align: center; color: red;'>-- Movie Recommendation System --</h1>", unsafe_allow_html=True)

st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

st.subheader(" Recommend Me Movie ")
## Loading Data
data=pd.read_csv(r"C:\Users\jitan\Referances\content_based movie recommendation system\movie_data.csv")
movies_name=data["title"].values

## Recommendation System
select=st.selectbox("Select A Movie Name : ",movies_name)
if st.button("Recommend Me"):
    st.subheader("Recommended Movies")
    recommend_movies=recommend.recommend(select)
    for movie in recommend_movies:
        st.success("ID:{} - {} ;Similarity'{}'".format(movie[0],movie[1],movie[2]))


## Sidebar
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: Black;'>-- Movie Details --</h2>", unsafe_allow_html=True)
    selected_id = st.sidebar.selectbox("Select Movie-ID :",utils.get_movie_id_list())
    get_details=st.button("Details")
    if get_details:
        st.dataframe(utils.get_movie_details_from_id(selected_id))

