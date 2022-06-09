import pandas as pd
import numpy as np

data=pd.read_csv(r"D:\Projects\Content-Based_Movie_Recommendation_System-main\Backend\Data\data_for_filtering.csv")
data.set_index("movie_id",inplace=True)


### Get Movie-ID List
def get_movie_id_list():
    movie_id_list=data.index.tolist()
    return sorted(movie_id_list)


### Get Movie Details From Movie-ID
def get_movie_details_from_id(id):
    """ Takes Movie-ID & returns dataframe of all available details of that movie """
    df=data.loc[id]
    dictionary={}
 
    dictionary["Name"]=df['title']
    dictionary["Rating"]=df['rating']
    dictionary["Genres"]=df['genres']
    dictionary["Cast"]=df['cast']
    dictionary["Director"]=df['director']
    dictionary["Producer"]=df['producer']
    dictionary["Budget"]=str(int(df["budget (in Million)"]))+" Million"
    dictionary["Lang"]=df['original_language']
    dictionary["Runtime"]=int(df['runtime'])
    dictionary["Spoken_languages"]=df['spoken_languages']
    dictionary["Production_company"]=df['production_companies'].split(",")[0]
    dictionary["Production_Country"]=df['production_countries'].split(",")[0]

    return pd.DataFrame([dictionary])
##
#details_df=get_movie_details_from_id(49026)
#print(details_df)