import requests
import json
get_session_id = requests.get('https://api.themoviedb.org/3/authentication/token/new?api_key=5cd843c18592532a3fdceb17ed37cb9d')
print(get_session_id.json())

guest_session = requests.get('https://api.themoviedb.org/3/authentication/guest_session/new?api_key=5cd843c18592532a3fdceb17ed37cb9d')
print(guest_session.json())

myKey = {"request_token": "6bc047b88f669d1fb86574f06381005d93d3517a"}

new_session = requests.get('https://api.themoviedb.org/3/authentication/session/new?api_key=5cd843c18592532a3fdceb17ed37cb9d')
print(new_session.json())
#Checking

