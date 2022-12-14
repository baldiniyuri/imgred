import schedule
import time
from resize.resize_function import Scheduling_Queue

def jog():
    print("Ok")
schedule.every(1).minutes.do(jog)


while True:
    schedule.run_pending()
    time.sleep(1) 