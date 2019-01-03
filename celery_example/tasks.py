from __future__ import absolute_import
from celery_example.celery import app

import time

@app.task
def longtask(x,y):
    print("Long task begins")
    time.sleep(5)
    print('long longtask finished')
    return x+y