import pandas as pd
import numpy as np

data=pd.read_csv(r"D:\Projects\Content-Based_Movie_Recommendation_System-main\Backend\Data\movie_data_recommendation_engine.csv")    # load (Movie-ID,title) data
# movies_name=data["title"].values                                                                                                     # load title
similarity_matrix=np.load(r"D:\Projects\Content-Based_Movie_Recommendation_System-main\Backend\Data\similarity_matrix.npy")          # load similarity matrix


def recommend(movie_name):
    """ Takes A movie name & Returns Top-3 similar list("movie_Id","movie_title","similarity) """
    Recommended_movies = []

    movie_index=data[data["title"]==(movie_name)].index[0]                                   # return movie_Id from movie name
    similarity=similarity_matrix[movie_index]
    recommend_movies=sorted(list(enumerate(similarity)),reverse=True,key=lambda x:x[1])[1:4] # return top-3 most similar(movie_Id,similarity_matrix)
    for movie in recommend_movies:
        Recommended_movies.append([movie[0],data.iloc[movie[0]].title,round(movie[1],2)])
    
    return Recommended_movies

# movies=recommend("Pirates of the Caribbean: On Stranger Tides")
# movies=recommend("Furious 7")
# for movie in movies:
#     print("ID:{} - {} ;Similarity'{}'".format(movie[0],movie[1],movie[2]))
