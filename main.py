import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, redirect, url_for, flash, render_template, request, session

session = requests.session()
app = Flask(__name__)
app.secret_key = "xQgA3014gga442s"

@app.route("/")
def home():
    return render_template("index.html")

def get_best_new_albums(param1, var1):
    """ get product name by ASOS' html element, accepting url as param1 """
    global session
    headers = {
        'authority': 'www.pitchfork.com',
        'method': 'GET',
        'scheme': 'https',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }
    html = requests.get(param1, headers=headers).text
    soup = bs(html, 'html.parser')
    wraps = soup("a", {"class": "link-block"})

    for wrap in wraps:
        var1.append(wrap)



if __name__ == "__main__":
    url = "https://pitchfork.com/best/"
    results = []
    get_best_new_albums(url, results)
    app.run(debug=True)
