import requests
import environ
import os

root = environ.Path(__file__) - 3

env = environ.Env()
environ.Env.read_env(os.path.join(root, '.env'))     # reading .env file

# url open API holder
remote_url = env.str('OPEN_API')


def download_json():
    return requests.request("GET", remote_url).json()
