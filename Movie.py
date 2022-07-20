import requests
import json
import pandas as pd
import sqlalchemy as db	


def movie_search(movie_input):
        i = 0
        request = requests.get('https://api.themoviedb.org/3/search/movie?api_key=ca247a677e49a57329443e35dfc24974&language=en-US&page=1&query={}&include_adult=false'.format(movie_input)).json()
        try:
            while i < len(request):
                print(request['results'][i]['original_title'], request['results'][i]['release_date'])
                i += 1
        except IndexError:
            print('No movies for this search')

def movie_list(movie_input):
        i = 0
        movies = []
        request = requests.get('https://api.themoviedb.org/3/search/movie?api_key=ca247a677e49a57329443e35dfc24974&language=en-US&page=1&query={}&include_adult=false'.format(movie_input)).json()
        try:
            while i < len(request):
                movies.append(tuple((request['results'][i]['original_title'], request['results'][i]['release_date'])))
                i += 1
            return movies
        except IndexError:
            return 'No movies for this search'

def movie_database(movie_input):
    """Adding the list of movies to a database"""
    m_list = []
    releaz = []
    for each_movie in movie_list(movie_input):
        m_list.append(each_movie[0])
        releaz.append(each_movie[1])
    print(m_list)
    print(releaz)
    data = {"Names":m_list, "Release":releaz}
    my_data_frame = pd.DataFrame(data)
    engine = db.create_engine('sqlite:///movies.db')
    my_data_frame.to_sql('data', con=engine, if_exists='append', index=False)
    col_names = ['Movie Title', 'Release']
    query_result = engine.execute("SELECT * FROM data;").fetchall()
    return pd.DataFrame(query_result, columns = col_names)

def clear_data(movie_input):
    """Clearing the data"""
    data = {"Names": [], "Release": []}
    my_data_frame = pd.DataFrame(data)
    engine = db.create_engine('sqlite:///movies.db')
    my_data_frame.to_sql('data', con=engine, if_exists='replace', index=False)
    col_names = ['Movie Title', 'Release']
    query_result = engine.execute("SELECT * FROM data;").fetchall()
    return pd.DataFrame(query_result, columns = col_names)

if __name__ == '__main__':
    movie_input = str(input('Search for movie or "no" to exit when prompted: '))
    while movie_input != ('no' or 'No'):
        movie_search(movie_input)
        print(movie_list(movie_input))
        print(movie_database(movie_input))
        print('Search for another movie?')
        movie_input = str(input())
    clear_data(movie_input)