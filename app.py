from flask import Flask, redirect, render_template, request, url_for
import datetime
from covid_uk import covid_uk
import service
from db import DB
from update import Update
from comment import Comment

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/coviduk', methods=["GET", "POST"])
def coviduk():
    if request.method == 'GET':
        #current_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        update = service.get_nations_data()
        return render_template('covid.html', release_date=Update.release_date, update=update, comments=DB.comments)
    comment = service.create_comment(request)
    DB.comments.append(comment)
    return redirect(url_for('coviduk'))


if __name__ == '__main__':
    app.run()
