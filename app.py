import csv
import flask
from flask import json, send_file
import requests

from flask import request, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/recall', methods=['POST'])
def searchRecalls():
    searchString = str(request.form.get('search_string'))
    searchField = str(request.form.get('search_field'))
    limit = str(request.form.get('max_result'))

    url = "https://api.fda.gov/device/recall.json"
    params = [('search', searchField + ":" + searchString), ('limit', limit)]
    #address = "https://api.fda.gov/device/recall.json?search=" + searchField + ":" + searchString + "&limit=" + str(limit)
    
    response = requests.get(url, params=params)
    data = response.json()
    results = data['results']

    path = './tmp/items.csv'

    #create CSV. Needs to be adapted
    with open('./tmp/items.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)

        for item in results:
            writer.writerow(item.values())

    return send_file(path, mimetype='text/csv', download_name='items.csv', as_attachment=True)


app.run(host='0.0.0.0')