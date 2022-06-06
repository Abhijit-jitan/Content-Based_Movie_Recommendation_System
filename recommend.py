import pandas as pd
import numpy as np

data=pd.read_csv(r"C:\Users\jitan\Referances\content_based movie recommendation system\movie_data.csv")
movies_name=data["title"].values
similarity_matrix=np.load(r"C:\Users\jitan\Referances\content_based movie recommendation system\similarity_matrix.npy")


def recommend(movie_name):
    """ Takes A movie name & Returns Top-5 similar Movie_Dictionary("movie_Id":"movie_title")"""
    Recommended_movies = {}

    movie_index=data[data["title"]==(movie_name)].index[0] # return movie_Id from movie name
    similarity=similarity_matrix[movie_index]
    recommend_movies=sorted(list(enumerate(similarity)),reverse=True,key=lambda x:x[1])[1:6] # return top-5 most similar(movie_Id,similarity_matrix)
    for movie in recommend_movies:
        Recommended_movies[movie[0]]=data.iloc[movie[0]].title

    return Recommended_movies



"""
recommended_movies_dict=recommend("Pirates of the Caribbean: On Stranger Tides")
for k,v in recommended_movies_dict.items():
    print('ID:{}:: movie:{}'.format(k,v))
"""