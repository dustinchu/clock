from apscheduler.schedulers.blocking import BlockingScheduler
import requests

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    r = requests.get('https://www.google.com.tw/')
    if r.status_code == requests.codes.ok:
        print("OK")
sched.start()