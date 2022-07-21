# Main file for our APIs

import requests
import json
import pandas as pd
import sqlalchemy as db
import Spotify
import Sports_News
import Movie
import TV


def get_genre():
  genre = str(input('Please input the media genre: (Music, Movies, TV, or Sports)'))
  if genre == 'Music':
    Spotify.main()
  elif genre == 'Movies':
    Movie.main()
  elif genre == 'TV':
    TV.main()
  elif genre == 'Sports':
    Sports_News.main()
  else:
    print('Invalid genre entered. Please try again: ')

def main():
  user_input = str(input('Would you like to find some media?')).lower()
  while user_input != 'no':
    get_genre()
    print('Search for more media?')
    user_input = str(input()).lower()


if __name__ == '__main__':
  main()
