# a Flask based on the tutorials from Neural9 on Youtube

DEBUG=True

from flask import Flask, request, make_response, render_template

app = Flask(__name__)



@app.route('/')
def index():
    myval='neural9'
    myresult = 10 + 20
    mylist = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
    return render_template('index.html', list = mylist)


@app.route('/2')
def page2():
    return render_template('page2.html')

@app.route('/hello')
def hello():
    response = make_response('Hello World\n')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response

@app.route('/login/<name>')
def login(name):
    return f'<h3>Logging in {name}.'

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
