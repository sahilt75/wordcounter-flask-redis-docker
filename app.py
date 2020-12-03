import redis
from flask import Flask,request
from flask_restx import Resource, Api, fields
import os
from utils import marshal_response

# App configs
app = Flask(__name__)
api = Api(app, version='1.0', title='Word counter API',
    description='A simple word counter with flask and redis',
)
ns = api.namespace('word', description='Word operations')
cache = redis.Redis(host=os.getenv('REDIS_HOST','redis'), port=6379,decode_responses=True)


@ns.route('/<word>',methods=['GET','PUT'])
@ns.param('word', 'The word identifier (case-insensitive)')
class WordCounter(Resource):
    @ns.doc('Get word counter')
    def get(self,word):
        """Get count of a word"""
        count = cache.get(word.lower())
        if count:
            return marshal_response(200,'Word `{}` has been PUT {} times'.format(word,count),'SUCCESS'),200
        else:
            return marshal_response(404,'Oops! word `{}` not found'.format(word),'ERROR'),200

    @ns.doc('Increment word counter')
    def put(self,word):
        """Increment count of a word"""
        cache.incr(word.lower())
        return marshal_response(200, 'Counter incremented for `{}`!'.format(word), 'Success'),200




