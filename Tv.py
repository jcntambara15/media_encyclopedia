import requests
import pandas as pd
import sqlalchemy as db	
import json

def tv_search(t):
    i = 0
    r = requests.get('https://api.themoviedb.org/3/search/tv?api_key=ca247a677e49a57329443e35dfc24974&language=en-US&page=1&query={}&include_adult=false'.format(t)).json()
    while i < len(r):
        print(r['results'][i]['original_name'])
        i += 1
        


if __name__ == '__main__':
    t = str(input('Search for TV Show or "no" to exit when prompted: '))
    while t != ('no' or 'No'):
        tv_search(t)
        print('Would you like to search for another show?')
        t = str(input())