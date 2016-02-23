import time
import datetime
from celery import Celery
import random


app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')


@app.task
def write_file():
    time.sleep(random.randint(5, 12))
    with open('/Users/joe/Documents/livecoding/celery/slowwrite.txt', 'a') as outfile:
        outfile.write("{}\n".format(datetime.datetime.now().strftime("%h-%m-%s")))
