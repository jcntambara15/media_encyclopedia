import requests
import pandas as pd
import sqlalchemy as db	
import json


col_names = ['Title', 'Release Date']
df = pd.DataFrame(columns=col_names)

def tv_search(tv_input):
    i = 0
    request = requests.get('https://api.themoviedb.org/3/search/tv?api_key=ca247a677e49a57329443e35dfc24974&language=en-US&page=1&query={}&include_adult=false'.format(tv_input)).json()
    try:
        while i < len(request):
            '''print(request['results'][i]['original_name'], request['results'][i]['first_air_date'], request['results'][i]['id'])'''
            df.loc[len(df.index)] = [request['results'][i]['original_name'], request['results'][i]['first_air_date']]
            i += 1
    except IndexError:
        print('No shows for this search')
    for i in range(len(df)):
         print(df.loc[i, :].to_string())


'''def tv_list(tv_input):
        i = 0
        tv = []
        request = requests.get('https://api.themoviedb.org/3/search/tv?api_key=ca247a677e49a57329443e35dfc24974&language=en-US&page=1&query={}&include_adult=false'.format(tv_input)).json()
        try:
            while i < len(request):
                tv_data = [request['results'][i]['original_name'], request['results'][i]['first_air_date']]
                tv.append(tv_data)
                i += 1
            return tv
        except IndexError:
            return 'No movies for this search'''

'''def tv_database(tv_input):
    """Adding the list of shows to a database"""
    show_list = []
    for i in tv_list(tv_input):
        show_list.append(i)
    print(show_list)
    data = {"Names":tv_list(tv_input)}
    my_data_frame = pd.DataFrame(data)
    engine = db.create_engine('sqlite:///tv.db')
    my_data_frame.to_sql('data', con=engine, if_exists='append', index=False)
    col_names = ['Show Title', 'Release Date']
    query_result = engine.execute("SELECT * FROM data;").fetchall()
    return pd.DataFrame(query_result, columns = col_names)

def clear_data(movie_input):
    """Clearing the data"""
    data = {"Names": []}
    my_data_frame = pd.DataFrame(data)
    engine = db.create_engine('sqlite:///tv.db')
    my_data_frame.to_sql('data', con=engine, if_exists='replace', index=False)
    col_names = ['Show Title', 'Release Date']
    query_result = engine.execute("SELECT * FROM data;").fetchall()
    return pd.DataFrame(query_result, columns = col_names)'''


if __name__ == '__main__':
    tv_input = str(input('Search for TV Show or "no" to exit when prompted: '))
    while tv_input != ('no' or 'No'):
        tv_search(tv_input)
        print('Search for another show?')
        tv_input = str(input())
