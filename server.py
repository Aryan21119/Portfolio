import csv

from flask import Flask, render_template, request

app = Flask(__name__)


def write_csv(data):
    with open('data.csv', mode='a', newline='') as csvfile:
        email = data['email']
        subject = data['subject']
        text = data['text']
        writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([email, subject, text])


@app.route("/")
def index_html():
    return render_template("index.html")


@app.route("/<string:link_name>")
def link_name_html(link_name):
    return render_template(link_name)


@app.route('/info.html', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_csv(data)
    else:
        print("something went wrong")
    return render_template("info.html")






