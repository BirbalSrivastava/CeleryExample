from __future__ import absolute_import
from celery import Celery

app = Celery('celery_example', broker='amqp://yash:yash786@localhost/yash_vhost', backend='rpc://', include=['celery_example.tasks'])