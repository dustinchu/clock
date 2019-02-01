
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=59)
def timed_job():
    r = requests.get('https://bankyou.herokuapp.com/news')
    if r.status_code == requests.codes.ok:
        print("OK")
    print('This job is run every 59 minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()