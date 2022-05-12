import requests
from django.conf import settings


def fetch_movie(title):
    """
    This function basically fetches a movie by title from the omdb database
    :param: string

    """
    my_api_key = settings.API_KEY
    url = f"http://www.omdbapi.com/?t={title}&type=movie&apikey={my_api_key}"
    response = requests.get(url)
    return response
