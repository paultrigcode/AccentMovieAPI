import requests
from django.conf import settings
from requests.exceptions import ConnectionError, RequestException, Timeout


class MovieAPIConnectionException(Exception):
    pass


class MovieAPINotFoundException(Exception):
    pass


def fetch_movie(title: str):
    """Fetch a movie by title from omdb database"""
    api_url = f"http://www.omdbapi.com"
    params = {"apikey": settings.API_KEY, "type": "movie", "t": title}

    try:
        response = requests.get(api_url, params=params)
        data = response.json()
    except (ConnectionError, Timeout, RequestException):
        raise MovieAPIConnectionException("Error connecting to imdb API.")

    if response.status_code == requests.codes.ok and data["Response"] == "False":
        raise MovieAPINotFoundException("A movie with that title does not exist.")

    return data
