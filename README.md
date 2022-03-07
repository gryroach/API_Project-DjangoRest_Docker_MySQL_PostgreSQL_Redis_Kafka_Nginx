# API_Project-DjangoRest_Docker_MySQL_PostgreSQL_Redis_Kafka_Nginx
Django REST framework project for administration and synchronization of posts from open API.

## Functionality
- synchronization of posts from open API
- synchronization of posts authors
- CRUD endpoints for authors

As example of open API is data from [JSONPlaceholder](https://jsonplaceholder.typicode.com/)

### Project contains two main directories:
- drf_project - files for basic functions of projet
- logs - files for logging of work django project


#### services of drf_project:
- web (django rest project)
- db (MySQL database)
- redis (data caching)

#### services of logs:
- logs (django project for logging)
- dblogs (PostgreSQL database)
- kafka (stream processing system)
- zookeeper (to ensure the work of kafka)
- nginx (required to work as a Gunicorn reverse proxy)

## Launch of the project

The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/gryroach/API_Project-DjangoRest_Docker_MySQL_PostgreSQL_Radis_Kafka_Nginx.git
$ cd API_Project-DjangoRest_Docker_MySQL_PostgreSQL_Radis_Kafka_Nginx
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install virtualenv
$ python3 -m venv env
$ source env/bin/activate
```

Install the dependencies for django project:
```sh
(env)$ pip install -r ./drf_project/requirements.txt
```
Install the dependencies for logs:
```sh
(env)$ pip install -r .logs/django_logs/requirements.txt
```
The .env files already exist for the example, but you can change them:
- env-file for django project:
```sh
(env)$ nano .env
```
- env-file for loggs:
```sh
(env)$ nano logs/.env.logs
```
```POSTS_API``` and ```AUTHORS_API``` are the URLs for open API respectively

After that, start the logs docker-compose to run kafka broker and log-server:

```sh
(env)$ docker-compose -f logs/docker-compose.yml up --build -d
```
When the log-server will be started, run projects docker-compose file:
```sh
(env)$ docker-compose -f docker-compose.yml up --build -d
```

Create superusers for project:
```sh
(env)$ docker-compose exec web python manage.py createsuperuser
```
Create superusers for log:
```sh
(env)$ cd logs
(env)$ docker-compose exec logs python manage.py createsuperuser
```

## Work
Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see available urls.

> **NOTE**: **Before syncing posts for the first time, sync authors**

After any synchronization, a record is made in the database logs with information about the type of synchronization. 

To see these entries, go to the address [http://localhost:1337/admin/](http://localhost:1337/admin/) and log in as a user.
