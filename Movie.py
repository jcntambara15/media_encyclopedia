import requests
import json


def movie_search(m):
        i = 0
        r = requests.get('https://api.themoviedb.org/3/search/movie?api_key=ca247a677e49a57329443e35dfc24974&language=en-US&page=1&query={}&include_adult=false'.format(m)).json()
        try:
            while i < len(r):
                print(r['results'][i]['original_title'])
                i += 1
        except IndexError:
            print('No movies for this search')

if __name__ == '__main__':
    m = str(input('Search for movie or "no" to exit when prompted: '))
    while m != ('no' or 'No'):
        movie_search(m)
        print('Search for another movie?')
        m = str(input())