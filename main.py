"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from filewrite_module import write_file
from searchjobs_module import searchjobs
from flask import Flask, render_template, request, redirect, send_file

app = Flask("Day-Thirteen-and-Fourteen")
db = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    term = request.args.get("term")

    if not db.get(term):
        db[term] = searchjobs(term)
    
    return render_template("search.html",term=term, len_term=len(db[term]),results=db[term])

@app.route("/export")
def export():
    
    try:
        term = request.args.get("term")
        if not term:
            raise Exception()
        term = term.lower()
        if not db.get(term):
            raise Exception()
        write_file(term,db[term])
        # return send_file(term + ".csv")
        # raise Exception()
    except:
        return redirect("/")
    # if not db.get(term):
    #     db[term] = searchjobs(term)
    
    # return render_template("search.html",term=term, len_term=len(db[term]),results=db[term])


app.run(host="0.0.0.0")