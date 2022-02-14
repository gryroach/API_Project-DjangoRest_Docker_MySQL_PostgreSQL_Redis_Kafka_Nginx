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
            result['Number of updated authors'] += 1
        except IndexError:
            result['Number of downloaded authors'] += 1
            result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        # try:
        #     serializer = AuthorSerializer(data=author)
        #
        #     if serializer.is_valid(raise_exception=True):
        #         inst = list(filter(lambda item: getattr(item, 'id') == author['id'], ex_authors))[0]
        #         serializer.create(serializer.validated_data)
        #         # inst = Author(**serializer.validated_data)
        #         # print(inst)
        #         # inst.save()
        #         # instance = Author(**serializer.validated_data)
        #         # serializer.save()
        #         # instance.save()
        #
        #         # Author.objects.update(**serializer.validated_data)
        #     # inst = list(filter(lambda item: getattr(item, 'id') == author['id'], ex_authors))[0]
        #     # for (key, value) in author.items():
        #     #     setattr(inst, key, value)
        #     # inst.update_date = datetime.datetime.now()
        #     result['Number of updated authors'] += 1
        #     result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # except IndexError:
        #     serializer = AuthorSerializer(data=author)
        #
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save()
        #         new_data.append(serializer.validated_data)
        #     # for (key, value) in author.items():
        #     #     setattr(inst, key, value)
        #     # inst.save()
        #
        #     # inst.update_date = datetime.datetime.now()
        #     # new_data.append(inst)
        #     result['Number of downloaded authors'] += 1
        #     result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        # except KeyError:
        #     return Response(data="There is no data on the remote API server", status=400)

    # Post.objects.bulk_update_or_create(ex_authors, ['name', 'username', 'email', 'phone', 'website', 'address', 'company', 'update_date'], match_field='id')
    # Author.objects.bulk_update_or_create(new_data, ['id', 'name', 'username', 'email', 'phone', 'website', 'address', 'company', 'update_date'], match_field='username')
    # Author.objects.bulk_create(new_data)
    return Response(result)
