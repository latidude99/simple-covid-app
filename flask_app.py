from flask import Flask
from covid_uk import covid_uk

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'latidude99 python web playground'


@app.route('/covid_uk')
def cov_uk():
    return covid_uk()



