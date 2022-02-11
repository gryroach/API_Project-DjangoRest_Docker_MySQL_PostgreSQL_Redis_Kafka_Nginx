import datetime
from rest_framework.response import Response
from ..models import Post


def sinc_posts(posts, ex_posts):
    result = {
        'Number of downloaded posts': 0,
        'Number of updated posts': 0,
        'Last update': ''
    }
    if isinstance(posts, dict):
        posts = [posts]

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
            inst = Post()
            for (key, value) in post.items():
                setattr(inst, key, value)
            inst.update_date = datetime.datetime.now()
            new_data.append(inst)
            result['Number of downloaded posts'] += 1
            result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        except KeyError:
            return Response(data="There is no data on the remote API server", status=400)

    Post.objects.bulk_update_or_create(ex_posts, ['userId', 'title', 'body', 'update_date'], match_field='id')
    Post.objects.bulk_update_or_create(new_data, ['userId', 'title', 'body', 'update_date'], match_field='id')

    return Response(result)


def sync_authors(authors, ex_authors):
    result = {
        'Number of downloaded authors': 0,
        'Number of updated authors': 0,
        'Last update': ''
    }
    if isinstance(authors, dict):
        authors = [authors]

    new_data = []
