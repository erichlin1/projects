from flask import Flask,request

## main project file

## import auth_Helper.py


## 1. Retrieve authorization code
## 2. Exchange authorization code for access token

## etsy_scope = ["transaction_r"]

## Create callback URL via flask 

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def callback_url():
    ## copy and paste state and code URL parameters that Etsy's 404 URL returns
    return request.args


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, ssl_context =('cert.pem'))
