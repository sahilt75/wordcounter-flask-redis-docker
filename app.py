import redis
from flask import Flask,request
from flask_restx import Resource, Api
import os

from utils import marshal_response

app = Flask(__name__)
api = Api(app, version='1.0', title='Word counter API',
    description='A simple word counter with flask and redis',
)
ns = api.namespace('words', description='Word operations')
cache = redis.Redis(host=os.getenv('REDIS_HOST','redis'), port=6379,decode_responses=True)


@ns.route('/word/<word>',methods=['GET','PUT'])
class WordCounter(Resource):
    def get(self,word):
        count = cache.get(word)
        if count:
            return marshal_response(200,'Word `{}` has been PUT {} times'.format(word,count),'SUCCESS')
        else:
            return marshal_response(404,'Oops! word `{}` not found'.format(word),'ERROR')

    def put(self,word):
        cache.incr(word)
        return marshal_response(200, 'Counter incremented for `{}`!'.format(word), 'Success')




