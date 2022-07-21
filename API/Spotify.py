import requests
import os
import json


CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}

BASE_URL = 'https://api.spotify.com/v1/'


def playlist_search(user_choice, user_id):
  querystring = {"limit":"10","offset":[user_choice]}  
  response = requests.get(BASE_URL + 'users/' + user_id + '/playlists', headers=headers,params=querystring).json()
  try:
    pl_name=response['items'][0]['name']
    pl_link=response['items'][0]['external_urls']
    print(pl_name, pl_link)
  except IndexError:
    print("User playlist count insufficient, try again.")


def main():
  user_cont = int(input("Do you wish to get a playlist from your spotify? \n 1.Yes \n 2.No \n"))
  while user_cont ==  1:
    user_id = input('Enter user id: ')
    user_choice = int(input("Choose a random number between 1 and 10:"))
    playlist_search(user_choice, user_id)
    user_cont = int(input("Do you wish to get another playlist from your spotify? \n 1.Yes \n 2.No \n"))


if __name__ == "__main__":
  main()