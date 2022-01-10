import datetime
import requests
import environ
import os
from json import JSONDecodeError

from django.http import HttpResponseBadRequest
from rest_framework.response import Response

from .models import JPHModel
from .serializers import JPHModelSerializer

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
    ex_posts_dict = ex_posts.values()
    for post in posts:
        try:
            inst_id = list(filter(lambda item: item['id'] == post['id'], ex_posts_dict))[0]['id']
            inst = ex_posts[inst_id - 1]
            serializer = JPHModelSerializer(instance=inst, data=post)
            result['Number of updated posts'] += 1
        except IndexError:
            serializer = JPHModelSerializer(data=post)
            result['Number of downloaded posts'] += 1
        except KeyError:
            return Response(data="There is no data on the remote API server", status=400)
        if serializer.is_valid():
            serializer.save()
            result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            return Response(serializer.errors, status=400)
    return Response(result)


def sinc_posts2(posts, ex_posts):
    result = {
        'Number of downloaded posts': 0,
        'Number of updated posts': 0,
        'Last update': ''
    }
    if isinstance(posts, dict):
        posts = [posts]
    if not isinstance(posts, list):
        raise TypeError
    data = []
    for post in posts:
        try:
            inst = list(filter(lambda item: getattr(item, 'id') == post['id'], ex_posts))[0]
            for (key, value) in post.items():
                setattr(inst, key, value)
            inst.update_date = datetime.datetime.now()
            result['Number of updated posts'] += 1
        except IndexError:
            data.append(post)
            result['Number of downloaded posts'] += 1
        except KeyError:
            return Response(data="There is no data on the remote API server", status=400)

    JPHModel.objects.bulk_update(ex_posts, ['userId', 'title', 'body', 'update_date'])

    # for new
    serializer = JPHModelSerializer(data=data, many=True)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=400)

    result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return Response(result)


