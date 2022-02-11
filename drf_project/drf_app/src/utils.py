import requests
from json import JSONDecodeError

from django.http import HttpResponseBadRequest


def download_json(url):
    try:
        return requests.request("GET", url).json()
    except requests.exceptions.ConnectionError:
        return HttpResponseBadRequest("The remote api server is not responded.")
    except KeyError:
        return HttpResponseBadRequest("The remote api server address is not valid.")
    except JSONDecodeError:
        return HttpResponseBadRequest(f"Failed to get data from the server by {url}.")
    except requests.exceptions.MissingSchema:
        return HttpResponseBadRequest("Invalid OPEN_API.")



