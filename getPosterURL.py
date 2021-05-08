import requests, json

def getPosterURL(imdb_id):
    url = f'https://api.themoviedb.org/3/find/{imdb_id}?api_key=2bb89f5e38215f75ec3c5bdfc756831a&external_source=imdb_id'
    #url = f'http://www.omdbapi.com/?i={x.imdb_title_id}&apikey=15afbee'
    result = requests.get(url).json()
    try:
        poster_path = result['movie_results'][0]['poster_path']
    except IndexError:
        return "None1"
    if poster_path is None:
        return "None2"
    poster_url = f'https://image.tmdb.org/t/p/original{poster_path}'
    return poster_url
