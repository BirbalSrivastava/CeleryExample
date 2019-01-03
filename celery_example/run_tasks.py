from celery_example.tasks import longtask
import time

if __name__ == '__main__':
    result = longtask.delay(1,3)
    print("Task finished ? ", result.ready())
    print("Task result: ", result.result)
    time.sleep(10)
    print("task finished? ", result.ready)
    print("Task result: ",result.result)



