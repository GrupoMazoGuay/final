# This Python file uses the following encoding: utf-8
from flask import Flask
from db_connection import DBConnection
from flask import render_template, request
from url_scrapper import Scrapper
from pymongo.errors import ConnectionFailure
from collections import Counter
import urllib2
from stop_words import get_stop_words

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    error = None
    if request.method == "POST":
        dbconnection = DBConnection()
        conn = dbconnection.mongodb_conn()

        if request.form['text-box'] == '':
            return '', 204

        URL = request.form['text-box']
        URL = URL.replace(" ", "")

        dataSplited = list()

        if (URL.endswith('.txt')):
            # parseo los datos y los subo
            print "lalal"
            scrapper = Scrapper(URL)
            print "lalal1"
            scrapper.get_data()
            print "lalal2"
            scrapper.parse_data()
            print "lala3"

            print scrapper.dictOfWords

            if conn is not None:
                for key in scrapper.dictOfWords.keys():
                    dbconnection.save_in_database(
                        key, scrapper.dictOfWords[key])

            print "posting data"

        words = list()

        # recojo los datos y los muestro
        if conn is not None:
            words = dbconnection.get_all_data_from_database()
            for word in words:
                results.append(word)
        else:
            error = "Database is down."
            print error

    return render_template('index.html', results=results, error=error)


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    results = []
    error = None
    dbconnection = DBConnection()
    conn = dbconnection.mongodb_conn()
    if conn is not None:
        dbconnection.delete_database()
    return render_template('index.html', results=results, error=error)

if __name__ == "__main__":
    app.run(host='localhost', port=8080)
