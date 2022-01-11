import datetime
import requests
import environ
import os
from json import JSONDecodeError

from django.http import HttpResponseBadRequest
from rest_framework.response import Response

from .models import JPHModel

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


def sinc_posts(posts, ex_posts):
    result = {
        'Number of downloaded posts': 0,
        'Number of updated posts': 0,
        'Last update': ''
    }
    if isinstance(posts, dict):
        posts = [posts]
    if not isinstance(posts, list):
        raise TypeError
    new_data = []
    for post in posts:
        try:
            inst = list(filter(lambda item: getattr(item, 'id') == post['id'], ex_posts))[0]
            for (key, value) in post.items():
                setattr(inst, key, value)
            inst.update_date = datetime.datetime.now()
            result['Number of updated posts'] += 1
            result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        except IndexError:
            inst = JPHModel()
            for (key, value) in post.items():
                setattr(inst, key, value)
            inst.update_date = datetime.datetime.now()
            new_data.append(inst)
            result['Number of downloaded posts'] += 1
            result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        except KeyError:
            return Response(data="There is no data on the remote API server", status=400)

    JPHModel.objects.bulk_update_or_create(ex_posts, ['userId', 'title', 'body', 'update_date'], match_field='id')
    JPHModel.objects.bulk_update_or_create(new_data, ['userId', 'title', 'body', 'update_date'], match_field='id')

    return Response(result)


