import time
from filewrite_module import write_file
from searchjobs_module import searchjobs
from flask import Flask, render_template, request, redirect, send_file
import os
from os.path import dirname, join
from db import db_connect
import json

app = Flask(__name__)

conn = db_connect()

cache = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    term = request.args.get("term")

    try:
        cache[term] = json.loads(conn.get(term))
    except:
        cache[term] = {}

    if not cache.get(term):
        cache[term] = searchjobs.apply_async(term)
        conn.set(term, json.dumps(searchjobs(term)))

    return render_template("search.html", term=term, len_term=len(cache[term]), results=cache[term])


@app.route("/export")
def export():
    try:
        term = request.args.get("term")
        if not term:
            raise Exception()
        term = term.lower()

        if not cache.get(term):
            raise Exception()

        write_file(term, cache[term])

    except:
        return redirect("/")

    return render_template("search.html", term=term, len_term=len(cache[term]), results=cache[term])


app.run()
