# a Flask based on the tutorials from Neural9 on Youtube

DEBUG=True

from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/hello')
def hello():
    response = make_response('Hello World\n')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response



@app.route('/login/<name>')
def login(name):
    return f'<h3>Logging in {name}.'

@app.route('/')
def index():
    return "<h3>Hello, World!<h3>"

@app.route('/add/<num1>/<num2>')
def add(num1, num2):
    try:
        return f"add {num1} to {num2}: result is {int(num1)+int(num2)}"
    except ValueError:
        return f"add {num1} to {num2}: result is {(num1)+(num2)}"
        
@app.route('/handle_url_params')
def handle_params():
    if user in request.args.keys() and msg in request.args.keys():
        user=request.args['user']
        msg=request.args['msg']
        return f"the following message will be left for {user}:<br>{msg}"
    else:
        return f"some parameters are missing!"







if __name__ == "__main__": app.run(host='0.0.0.0', port=4080, debug=DEBUG)
