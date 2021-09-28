import os

from dotenv import load_dotenv
from joblib import Parallel, delayed

load_dotenv()
API_TOKEN = os.getenv('GEN_TOKEN')

names = []

def get_lyrics(name, k):
  c = 0 
  import lyricsgenius as lg
  try:
    genius = lg.Genius(API_TOKEN,skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)
    songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs   
    s = [song.lyrics for song in songs]
    with open(f"api/data/{name}.txt", "w") as f:
      f.write("\n \n".join(s)) 
    c += 1
    print(f"Songs grabbed:{len(s)}")   
  except:   
    print(f"some exception at {name}: {c}")

songs = Parallel(n_jobs=20, verbose=1)(delayed(get_lyrics)(i, 5) for i in names)