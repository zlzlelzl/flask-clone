import time
from filewrite_module import write_file
from searchjobs_module import searchjobs
from flask import Flask, render_template, request, redirect, send_file
import os
from os.path import dirname, join
from db import db_connect
import json
from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
celery = Celery('tasks', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)

app = Flask(__name__)

conn = db_connect()

cache = {}


# @celery.task
# def add(x, y):
#     time.sleep(5)
#     return x + y


@ app.route("/")
def index():
    return render_template("index.html")


@ app.route("/search")
def search():
    term = request.args.get("term")

    try:
        cache[term] = json.loads(conn.get(term))
    except:
        cache[term] = {}

    if not cache.get(term):  # 비동기 갱신
        #     cache[term] = searchjobs.apply_async(term)
        task = searchjobs.delay(term).then
        print(task)
        # conn.set(term, json.dumps(searchjobs(term)))

    return render_template("search.html", term=term, len_term=len(cache[term]), results=cache[term])


@ app.route("/export")
def export():
    try:
        term = request.args.get("term")
        if not term:
            raise Exception()
        term = term.lower()

        if not cache.get(term):
            raise Exception()

        write_file(term, cache[term])
        # return send_file("11.txt", "w")

        # send_file(term + ".csv")
        # return send_file(term + ".csv")

    except:
        return redirect("/")

    return render_template("search.html", term=term, len_term=len(cache[term]), results=cache[term])


app.run()
