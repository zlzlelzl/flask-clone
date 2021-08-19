# tasks.py
import celery
from celery import Celery
import time
import random

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
app = Celery('tasks', broker=BROKER_URL, backend=CELERY_RESULT_BACKEND)


# @app.task
# def add(x, y):
#     return x + y


@celery.task(bind=True)
def mail_send_process(self, mail_list):
    with app.app_context():
        total = len(mail_list) - 1
        for idx, mail in enumerate(mail_list):
            # mail_send #
            time.sleep(2.0/random.randint(1, 4))
            self.update_state(state='PROGRESS', meta={
                              'current': idx, 'total': total})
        return {'current': idx, 'total': total}


print(mail_send_process)
