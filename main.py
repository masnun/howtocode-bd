# Imports

import requests, json
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/contrib/<repo>')
def contrib(repo):
    url = "https://api.github.com/repos/howtocode-com-bd/%s.howtocode.com.bd/contributors" % repo
    data = requests.get(url).json()

    for id, author in enumerate(data):
        data[id]['login'] = author['login'].replace("-", "--")
    return render_template('contrib.html', data=data)


if __name__ == '__main__':
    app.run()