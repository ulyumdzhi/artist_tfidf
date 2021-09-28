import os

from dotenv import load_dotenv
import lyricsgenius as lg

load_dotenv()
API_TOKEN = os.getenv('GEN_TOKEN')

def name_checker(name):
    # if name not in names:
    try:
        genius = lg.Genius(API_TOKEN,skip_non_songs=True, remove_section_headers=True)
        response = (genius.search_artist(name, max_songs=1, sort='popularity'))
        true_name = response.name
        return true_name  
    except:
        print(f"some exception at {name}")
    # return name


    


print(name_checker('black eyed pee'))