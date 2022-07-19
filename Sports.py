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
            1: ['Action Sports (X Games)', '/sports/action-sports'],
            2: ['Baseball (MLB)', '/sports/baseball/mlb'],
            3: ['Basketball (NCAA Mens)', '/sports/basketball/mens-college-basketball'],
            4: ['Basketball (NCAA Womens)', '/sports/basketball/womens-college-basketball'],
            5: ['Basketball (NBA)', '/sports/basketball/nba'],
            6: ['Basketball (WNBA)', '/sports/basketball/wnba'],
            7: ['Boxing', '/sports/boxing'],
            8: ['Football (NCAA)', '/sports/football/college-football'],
            9: ['Football (NFL)', '/sports/football/nfl'],
            10: ['Golf', '/sports/golf'],
            11: ['Hockey (NHL)', '/sports/hockey/nhl'],
            12: ['Horse Racing', '/sports/horse-racing'],
            13: ['MMA', '/sports/mma'],
            14: ['Olympic Sports', '/sports/olympics'],
            15: ['Racing', '/sports/racing'],
            16: ['Racing (NASCAR)', '/sports/racing/nascar'],
            17: ['Soccer', '/sports/soccer'],
            18: ['Tennis', '/sports/tennis']
        }
        print_menu(real_sports)
        return make_choice(real_sports)
    elif choice == 'fantasy':
        fantasy_sports = {
            1: ['Baseball', '/fantasy/baseball'],
            2: ['Basketball', '/fantasy/basketball'],
            3: ['Football', '/fantasy/football'],
            4: ['Hockey', ' /fantasy/hockey']
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
    base_url = 'http://api.espn.com/v1'
    return base_url + sport

def get_response(url) -> dict:
    """
    Making the request to the API and returning data as a parsed json file
    """
    pass

def main():
    sport = get_sport()
    url = create_url(sport)

if __name__ == "__main__":
    main()