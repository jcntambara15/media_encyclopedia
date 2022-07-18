# Main file for our APIs

import requests
import json
import pandas as pd
import sqlalchemy as db

def get_genre():
  genre = str(input('Please input the media genre (Music, Movies, TV, or Sports)': ))
  if genre == 'Music':
    return genre
  elif genre == 'Movies':
    return genre
  elif genre == 'TV':
    return genre
  elif genre == 'Sports':
    return genre
  else:
    genre = str(input('Invalid genre entered. Please try again: '))

def run_program():
  genre = get_genre()

if __name__ == '__main__':
  run_program()
  

