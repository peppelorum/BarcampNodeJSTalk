
import os

def get_secret_filepath(filename=''):
    return os.path.join('/static/secret/', filename)
