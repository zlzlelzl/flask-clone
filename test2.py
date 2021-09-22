from searchjobs_module import searchjobs
from celery import Celery
import time

celery = Celery("task", BROKER_URL="redis://localhost:6379",
                CELERY_RESULT_BACKEND='redis://localhost:6379/0')


@celery.task()
def add(a, b):
    time.sleep(5)
    return a+b


print(add(3, 4))
print(1)
