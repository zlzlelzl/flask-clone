import os
import sys
import time

from flask import Flask
from flask import request
from flask import jsonify


from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'],
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

celery = make_celery(app)

task_cache = dict()


@celery.task()
def add_together(a, b):
    time.sleep(5)
    return a+b


@app.route('/adder', methods=['GET'])
def adder():
    global task_cache
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    task = add_together.delay(a, b)
    task_cache[task.id] = task
    return task.id


@app.route('/progress', methods=['GET'])
def progress():
    global task_cache
    task_id = request.args.get('task_id')
    task = task_cache[task_id]
    return jsonify({
        'status': task.ready()
    })


@app.route('/result', methods=['GET'])
def result():
    global task_cache
    task_id = request.args.get('task_id')
    task = task_cache[task_id]
    return jsonify({
        'result': task.get()
    })
