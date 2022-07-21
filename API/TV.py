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
        while i < len(request['results']):
            df.loc[len(df.index)] = [request['results'][i]['original_name'], request['results'][i]['first_air_date']]
            i += 1
    except IndexError:
        print('No shows for this search')


def main():
    tv_input = str(input('Search for TV Show or "no" to exit when prompted: '))
    while tv_input != ('no' or 'No'):
        tv_search(tv_input)
        print('Search for another show?')
        tv_input = str(input())
    for i in range(len(df)):
        print(df.loc[i, :].to_string())
if __name__ == '__main__':
    main()
