import datetime
from rest_framework.response import Response
from django.core.cache import cache

from ..models import Post, Author
from ..serializers import AuthorSerializer, PostSerializer


def sync_objects(obj, ex_obj, type_object):
    result = {
        f'Number of downloaded {type_object}': 0,
        f'Number of updated {type_object}': 0,
        'Last update': ''
    }
    if isinstance(obj, dict):
        obj = [obj]

    new_data = []
    update_data = []
    for elem in obj:
        if type_object == 'posts':
            serializer = PostSerializer(data=elem)
        else:
            serializer = AuthorSerializer(data=elem)
        if serializer.is_valid(raise_exception=True):
            try:
                ex_inst = list(filter(lambda item: getattr(item, 'id') == elem['id'], ex_obj))[0]
                result[f'Number of updated {type_object}'] += 1
                result['Last update'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                update_data.append(serializer.create(validated_data=serializer.validated_data))
            except IndexError:
                result[f'Number of downloaded {type_object}'] += 1
                new_data.append(serializer.create(validated_data=serializer.validated_data))

    if type_object == 'posts':
        Post.objects.bulk_create(new_data)
        Post.objects.bulk_update([Post(userId=values.userId, id=values.id, title=values.title,
                                       body=values.body, update_date=values.update_date)
                                  for values in update_data], ['userId', 'title', 'body', 'update_date'],
                                 batch_size=1000)
    else:
        Author.objects.bulk_create(new_data)
        Author.objects.bulk_update([Author(id=values.id, name=values.name, username=values.username,
                                           email=values.email, phone=values.phone,
                                           website=values.website, address=values.address,
                                           company=values.company, update_date=values.update_date)
                                    for values in update_data], ['name', 'username', 'email', 'phone', 'website',
                                                                 'address', 'company', 'update_date'], batch_size=1000)
        cache.delete('authors')
        for author in new_data + update_data:
            cache.delete(f'author {author.id}')

    return Response(result)
