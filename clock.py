# from apscheduler.schedulers.blocking import BlockingScheduler
# import requests
#
# sched = BlockingScheduler()
#
# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     r = requests.get('https://bankyou.herokuapp.com/news')
#     if r.status_code == requests.codes.ok:
#         print("OK")
#
# sched.start()

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()