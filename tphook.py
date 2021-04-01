from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    '''index route'''
    return "Hello world !"

@app.route('/hello/<name>')
def hello(name):
    '''hello/<name> route'''
    return "hello" + str(name)

if __name__ == "__main__":
    app.run()
