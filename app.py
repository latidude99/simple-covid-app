from flask import Flask, render_template
import datetime
from covid_uk import covid_uk
import service

app = Flask(__name__)

hits = 0

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/coviduk")
def nations():
    current_date = datetime.datetime.utcnow()
    update = service.get_nations_data()
    return render_template('main.html', current_date=current_date,  update=update)


if __name__ == '__main__':
    app.run()
