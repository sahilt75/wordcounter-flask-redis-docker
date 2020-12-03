def marshal_response(status,body,message):
    return {
        'StatusCode' : status,
        'Body' : body,
        'Message': message
    }