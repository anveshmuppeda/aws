import json
import os

def hello(event, context):

    return os.environ['FIRST_NAME']

