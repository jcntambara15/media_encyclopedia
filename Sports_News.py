import requests
import json

def print_menu(menu):
    """
    Helper function. Prints user menu.
    """    
    for key in menu.keys():
        print (key, '--', menu[key][0])

def make_choice(menu):
    """
    Returns the URL ending for the for the user-picked sport
    """
    choice = str(input("Enter a sport's number from the list below: "))
    for i in range(len(menu)):
        if int(choice) in menu.keys():
            choice = menu[int(choice)][1]
            return choice
        else:
            choice = input("Invalid format. Please enter a sport's number from the list below: ")

def get_sport():
    """
    Shows sport options to user and then prompts them to choose one.
    """
    real_sports = {
        1: ['Baseball (MLB)', '/sports/baseball/mlb/news'],
        2: ['Basketball (NCAA Mens)', '/sports/basketball/mens-college-basketball/news'],
        3: ['Basketball (NCAA Womens)', '/sports/basketball/womens-college-basketball/news'],
        4: ['Basketball (NBA)', '/sports/basketball/nba/news'],
        5: ['Basketball (WNBA)', '/sports/basketball/wnba/news'],
        6: ['Football (NCAA)', '/sports/football/college-football/news'],
        7: ['Football (NFL)', '/sports/football/nfl/news'],
        8: ['Hockey (NHL)', '/sports/hockey/nhl/news'],
        9: ['Soccer (EPL)', '/sports/soccer/eng.1/news'],
        10: ['Soccer (MLS)', '/sports/soccer/usa.1/news']
    }
    print_menu(real_sports)
    return make_choice(real_sports)

def create_url(sport) -> str:
    """
    Design the url to access the News and Headlines endpoint of the API
    """
    base_url = 'http://site.api.espn.com/apis/site/v2'
    return base_url + sport

def get_response(url) -> dict:
    """
    Making the request to the API and returning data as a parsed json file
    """
    i = 0
    request = requests.get(url).json()
    
    try:
        while i < len(request):
            print(f"Name: {request['articles'][i]['images'][0]['name']}")
            print(f"Description: {request['articles'][i]['images'][0]['caption']}")
            print(f"Link: {request['articles'][i]['links']['web']['href']}")
            print()
            i += 1
    except IndexError:
        print('No news for this search')

def main():
    sport = get_sport()
    url = create_url(sport)
    get_response(url)

if __name__ == "__main__":
    main()
