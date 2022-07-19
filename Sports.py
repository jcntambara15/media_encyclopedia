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
    Chooses a sport based on user preference
    """
    choice = str(input('Would you like to view real or fantasy sports today? ')).lower()
    if choice == 'real':
        real_sports = {
            1: ['Action Sports (X Games)', '/sports/action-sports/news'],
            2: ['Baseball (MLB)', '/sports/baseball/mlb/news'],
            3: ['Basketball (NCAA Mens)', '/sports/basketball/mens-college-basketball/news'],
            4: ['Basketball (NCAA Womens)', '/sports/basketball/womens-college-basketball/news'],
            5: ['Basketball (NBA)', '/sports/basketball/nba/news'],
            6: ['Basketball (WNBA)', '/sports/basketball/wnba/news'],
            7: ['Boxing', '/sports/boxing/news'],
            8: ['Football (NCAA)', '/sports/football/college-football/news'],
            9: ['Football (NFL)', '/sports/football/nfl/news'],
            10: ['Golf', '/sports/golf/news'],
            11: ['Hockey (NHL)', '/sports/hockey/nhl/news'],
            12: ['Horse Racing', '/sports/horse-racing/news'],
            13: ['MMA', '/sports/mma/news'],
            14: ['Olympic Sports', '/sports/olympics/news'],
            15: ['Racing', '/sports/racing/news'],
            16: ['Racing (NASCAR)', '/sports/racing/nascar/news'],
            17: ['Soccer', '/sports/soccer/news'],
            18: ['Tennis', '/sports/tennis/news']
        }
        print_menu(real_sports)
        return make_choice(real_sports)
    elif choice == 'fantasy':
        fantasy_sports = {
            1: ['Baseball', '/fantasy/baseball/news'],
            2: ['Basketball', '/fantasy/basketball/news'],
            3: ['Football', '/fantasy/football/news'],
            4: ['Hockey', ' /fantasy/hockey/news']
        }
        print_menu(fantasy_sports)
        return make_choice(fantasy_sports)
    else:
        choice = print('Invalid input. Please try again. ')
        get_sport()

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
    pass

def main():
    sport = get_sport()
    url = create_url(sport)
    print(url)

if __name__ == "__main__":
    main()
