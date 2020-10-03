from flask import Flask, redirect, render_template, request
import requests
import csv

app = Flask(__name__)

# index page
@app.route("/")
def index():
            
    return render_template("index.html")

# iframe checking connectivity to hosts in the CSV
@app.route("/connect_test")
def connect_test():

    categories = []
    host_labels = []
    results = []
    urls =[]

    with open('target_sites.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for entry in csv_reader:
            category = entry[0]
            host = entry[1]
            url = entry[2]
            
            categories.append(category)
            host_labels.append(host)
            urls.append(url)

            try:
                request = requests.get(url, verify=False)
                if request.status_code == 200:
                    results.append("Reachable")
            except:
                results.append("Unreachable")

    return render_template("connectivity.html", categories = categories, host_labels = host_labels, results = results, urls = urls)
