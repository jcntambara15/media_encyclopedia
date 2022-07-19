# Main file for our APIs

import requests
import json
import pandas as pd
import sqlalchemy as db

from Movie import movie_search()
from Tv import tv_search()

def get_genre():
  genre = str(input('Please input the media genre: (Music, Movies, TV, or Sports)'))
  if genre == 'Music':
    return genre
  elif genre == 'Movies':
    movie_search()
  elif genre == 'TV':
    tv_search()
  elif genre == 'Sports':
    return genre
  else:
    print('Invalid genre entered. Please try again: ')


if __name__ == '__main__':
  get_genre()
  