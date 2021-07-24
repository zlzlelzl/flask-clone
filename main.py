"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from searchjobs_module import searchjobs
from flask import Flask, render_template, request

app = Flask("Day-Thirteen-and-Fourteen")
db = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    term = request.args.get("term")

    urls = [f"https://stackoverflow.com/jobs?r=true&q={term}",
    f"https://weworkremotely.com/remote-jobs/search?term={term}",
    f"https://remoteok.io/remote-dev+{term}-jobs"]

    if not db.get(term):
        db[term] = searchjobs(urls)
    
    return render_template("search.html", results=db[term])

app.run(host="0.0.0.0")