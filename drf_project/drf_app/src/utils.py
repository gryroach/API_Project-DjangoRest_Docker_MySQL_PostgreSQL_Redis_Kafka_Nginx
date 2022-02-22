import requests
from json import JSONDecodeError

from django.http import HttpResponseBadRequest


def download_json(url):
    try:
        return requests.request("GET", url).json()
    except requests.exceptions.ConnectionError:
        raise Exception('The remote api server is not responded.')
    except KeyError:
        raise Exception("The remote api server address is not valid.")
    except JSONDecodeError:
        raise Exception(f"Failed to get data from the server by {url}.")
    except requests.exceptions.MissingSchema:
        raise Exception("Invalid OPEN_API.")



