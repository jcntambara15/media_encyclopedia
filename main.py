# Main file for our APIs

import requests
import json
import pandas as pd
import sqlalchemy as db


"""Pasting the code for movie recommendations based on movie id, we might need to change the id of a movie name/keyword
to allow better user experience."""

session_id= 'c72032122d67260cc02034445c4206ba96a84f0e'
list_id = '8209394'

session_id= 'c72032122d67260cc02034445c4206ba96a84f0e'
list_id = '8209391'

# request token used in retriving sesion id 
mykey ={'request_token': '00b55b48576f0ad50239e00e35a9acd0c7091d2f'}
# api_key
api_key ='dd1c306527d8caa33b2acb40c88ce2ae'

#parts for the creating a list
list_body = {'name': 'Movie recommendation', 'description': 'List of movies to be recommended', 'language': 'en'}
header = {'Content-Type': 'application/json;charset=utf-8'}
query_string ={'session_id': 'c72032122d67260cc02034445c4206ba96a84f0e'}

#prints the list id used to add recommended movies
listUrl = 'https://api.themoviedb.org/3/list?api_key=dd1c306527d8caa33b2acb40c88ce2ae'
#responseL = requests.post(listUrl, headers=header, json=list_body, params=query_string)
#print(responseL.json())

def movie_entry(id):
    # https://developers.themoviedb.org/3/movies/get-movie-recommendations
 sample = requests.get('https://api.themoviedb.org/3/movie/'+str(id)+'/recommendations?api_key=dd1c306527d8caa33b2acb40c88ce2ae&language=en-US&page=1').json();
 return sample

def get_movie_list(response):
    """Creating a list of movies"""
    list_movies = []
    for dict_item in response:
        list_movies.append(dict_item['title'])
    return list_movies

#returns a list of id from the list of recommended movies
def get_id_list(response):
    """Creating a list of ids"""
    list_ids = []
    for dict_item in response:
        list_ids.append(dict_item['id'])
    return list_ids

#returns streaming services for a movie in the U.S region
def get_watch(ids):
    watch_list =[]
    for id in ids: 
        watch_pro = requests.get('https://api.themoviedb.org/3/movie/'+str(id)+'/watch/providers?api_key=dd1c306527d8caa33b2acb40c88ce2ae').json();
        if 'results' in watch_pro and 'US' in watch_pro['results']and 'flatrate' in watch_pro['results']['US']:
            for i in range(len(watch_pro['results']['US']['flatrate'])):
                watch_list.append(watch_pro['results']['US']['flatrate'][i]['provider_name'])
    return watch_list

def create_database_for_movies(response):
    """Adding the list of movies to a database"""
    data = {"Names":get_movie_list(response), 'IDs':get_id_list(response)}
    my_data_frame = pd.DataFrame(data)
    engine = db.create_engine('sqlite:///movies.db')
    my_data_frame.to_sql('data', con=engine, if_exists='replace', index=False)
    col_names = ['Movie Title', 'Movie Id']
    query_result = engine.execute("SELECT * FROM data;").fetchall()
    return pd.DataFrame(query_result, columns = col_names)

def create_database_for_providers(response):
    "Adding the list of streaming services for each movie to a database"
    data = {"providers":get_watch(get_id_list(response))}
    df = pd.DataFrame(data)
    engine = db.create_engine('sqlite:///movies.db')
    df.to_sql('data', con=engine, if_exists='replace', index=False)
    col_names =['Streaming Services']
    return pd.DataFrame(engine.execute("SELECT * FROM data;").fetchall(), columns = col_names)

user_entry = input('enter a movie id:')
movies = movie_entry(user_entry)['results']
id_list = get_id_list(movies)
print(create_database_for_movies(movies))
print(create_database_for_providers(movies))
