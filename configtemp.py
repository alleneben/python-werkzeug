import os


classpath = 'classes'
endpoint = ''
apiusername = ''
apikey =''
api_id = ''
API_AUTH = ''

AUTH_KEY = ''
SVS_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SVS_PATH)
DATABASE_USER = ''
DATABASE_PWD = ''
DATABASE_NAME = ''
DATABASE_HOST = 'localhost'
DATABASE_STR = "host='%s' user='%s' password='%s' dbname='%s'" % (
    DATABASE_HOST, DATABASE_USER, DATABASE_PWD, DATABASE_NAME)