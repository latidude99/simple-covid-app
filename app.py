from flask import Flask, redirect, render_template, request, url_for
import datetime
from covid_uk import covid_uk
import service
from db import DB

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/coviduk', methods=["GET", "POST"])
def coviduk():
    if request.method == 'GET':
        current_date = datetime.datetime.utcnow()
        update = service.get_nations_data()
        return render_template('covid.html', current_date=current_date, update=update, comments=DB.comments)

    DB.comments.append(request.form['comment'])
    return redirect(url_for('coviduk'))


if __name__ == '__main__':
    app.run()
