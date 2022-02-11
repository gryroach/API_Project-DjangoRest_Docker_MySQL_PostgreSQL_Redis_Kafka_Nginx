import datetime
from rest_framework.response import Response
from ..models import Post, Author, Company, Address, Geo
from ..serializers import AuthorSerializer


def sync_posts(posts, ex_posts):
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
    for author in authors:
        try:
            inst = list(filter(lambda item: getattr(item, 'id') == author['id'], ex_authors))[0]
            for (key, value) in author.items():
                setattr(inst, key, value)
            inst.update_date = datetime.datetime.now()
            result['Number of updated authors'] += 1
            result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        except IndexError:
            serializer = AuthorSerializer(data=author)

            if serializer.is_valid(raise_exception=True):

                # instance = Author(**serializer.validated_data)

                print('!!!!!!!! before save')
                print(serializer.validated_data)
                serializer.save()
                # serializer.save()

                print('!!!!!!! after save')



                # new_data.append(instance)
            # for (key, value) in author.items():
            #     setattr(inst, key, value)
            # inst.save()

            # inst.update_date = datetime.datetime.now()
            # new_data.append(inst)
            result['Number of downloaded authors'] += 1
            result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        except KeyError:
            return Response(data="There is no data on the remote API server", status=400)

    # Post.objects.bulk_update_or_create(ex_authors, ['name', 'username', 'email', 'phone', 'website', 'address', 'company', 'update_date'], match_field='id')
    # Author.objects.bulk_update_or_create(new_data, ['name', 'username', 'email', 'phone', 'website', 'address', 'company', 'update_date'], match_field='id')

    return Response(result)
