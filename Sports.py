import requests
import json

def print_menu(menu):
    for key in menu.keys():
        print (key, '--', menu_options[key] )

def get_sport():
    choice = str(input('Would you like to view real or fantasy sports today? ')).lower()

    if choice == 'real':
        real_sports = {
            1: 'Baseball',
            2: 'Basketball',
            3: 'Soccer',
            4: 'Football',
            5: 'Exit'
        }
        print_menu(real_sports)

    elif choice == 'fantasy':
        fantasy_sports = {
            1: 'Baseball',
            2: 'Basketball',
            3: 'Football',
            4: 'Hockey',
            5: 'Exit'
        }
        print_menu(fantasy_sports)

    else:
        choice = str(input('Invalid input. Please try again (real or fantasy): '))

def create_url(sport) -> str:
    """
    Design the url to access the News and Headlines endpoint of the API
    """
    base_url = 'https://www.http://api.espn.com/v1'
    return base_url + '_______'

def get_response(url) -> dict:
    """
    Making the request to the API and returning data as a parsed json file
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

    return response.json()

def main():
    get_sport()

if "__name__" == "__main__":
    main()