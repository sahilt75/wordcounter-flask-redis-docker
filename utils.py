"""
This function prepares the response object and returns it
"""
def marshal_response(status,body,message):
    return {
        'status' : status,
        'body' : body,
        'message': message
    }

