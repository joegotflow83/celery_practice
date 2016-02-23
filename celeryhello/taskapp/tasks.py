import random
import time

from celeryhello.celery import app


@app.task
def stupid_math():
    time.sleep(random.randint(5, 15))
    return 9 ** 9
