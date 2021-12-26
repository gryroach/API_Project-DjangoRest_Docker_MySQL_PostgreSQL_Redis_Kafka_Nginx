import requests
import environ
import os
from json import JSONDecodeError

from django.http import HttpResponseBadRequest

root = environ.Path(__file__) - 3

env = environ.Env()
environ.Env.read_env(os.path.join(root, '.env'))     # reading .env file

# url open API holder
remote_url = env.str('OPEN_API')


def download_json():
    try:
        return requests.request("GET", remote_url).json()
    except requests.exceptions.ConnectionError:
        return HttpResponseBadRequest("The remote api server is not responded.")
    except KeyError:
        return HttpResponseBadRequest("The remote api server address is not valid.")
    except JSONDecodeError:
        return HttpResponseBadRequest(f"Failed to get data from the server by {remote_url}.")
    except requests.exceptions.MissingSchema:
        return HttpResponseBadRequest("Invalid OPEN_API.")
