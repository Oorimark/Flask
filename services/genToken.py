# from flask import Flask

from datetime import datetime
from string import punctuation
from random import shuffle
import time

# app = Flask(__name__);
# app.config['SECRET_KEY'] = 'hello'

def generate_token():
    gen_token = "abcdefghijklmnopqrstuvwxyz" + "0123456789"
    shuffle_gen_token = (list(gen_token))
        
    shuffle(shuffle_gen_token)
    token = ''.join(shuffle_gen_token)    
    return (token[ :6])


        
# generating token
def token_encode(username):
    try:
        import jwt
        token = jwt.encode({'username': username, 'exp': datetime.datetime.now() +
                         datetime.datetime(minute=30)}, 'mark');
        return token
    except:
        try:
            generate_token()
                
        except Exception as e:
            return e
    
    
    
def token_decode(token):
    import jwt
    decode_ = jwt.decode(token, 'mark')
    return decode_


# so = generate_token()
# print(so)
# print(token_encode("mark"))

# if __name__ == '__main__':
#     token_encode('markhoal')
#     app.run(debug=True)