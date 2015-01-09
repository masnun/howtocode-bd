# Imports

import requests
from flask import Flask, render_template, redirect

app = Flask(__name__)
#app.debug = True

@app.route("/")
def home():
    return redirect("http://howtocode.com.bd")

@app.route('/contrib/<repo>')
def contrib(repo):
    url = "https://api.github.com/repos/howtocode-com-bd/%s.howtocode.com.bd/contributors" % repo
    data = requests.get(url).json()

    for id, author in enumerate(data):
        data[id]['badge_login'] = author['login'].replace("-", "--")
        data[id]['commits_url'] = "https://github.com/howtocode-com-bd/%s.howtocode.com.bd/commits/master?author=%s" % (repo, author['login'])
    return render_template('contrib.html', data=data)


if __name__ == '__main__':
    app.run()