from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'just getting started'

if __name__ == '__main__':
    app.run()

