from resize.resize_function import Scheduling_Queue
from django_q.models import Schedule

Schedule.objects.create(
    func='app.tasks.start_schedule',  
    minutes=5,  
    repeats=-1  
)

def start_schedule():
    print("Runing schedule ...")
    Scheduling_Queue()