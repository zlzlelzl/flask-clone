from filewrite_module import write_file
from searchjobs_module import searchjobs
from flask import Flask, render_template, request, redirect, send_file
import os
from os.path import dirname, join

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev",
    DATABASE=join(dirname(dirname(__file__)), "db.sqlite3"),
)
db = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    term = request.args.get("term")

    if not db.get(term):
        db[term] = searchjobs(term)

    return render_template("search.html", term=term, len_term=len(db[term]), results=db[term])


@app.route("/export")
def export():
    try:
        term = request.args.get("term")
        if not term:
            raise Exception()
        term = term.lower()
        if not db.get(term):
            raise Exception()
        write_file(term, db[term])
        return send_file(term + ".csv")

    except:
        return redirect("/")


app.run(host="0.0.0.0")
