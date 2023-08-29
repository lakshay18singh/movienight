from django_celery_beat.models import PeriodicTask, IntervalSchedule

def schedule_setup():
    minute_schedule, created = IntervalSchedule.objects.get_or_create(period=IntervalSchedule.MINUTES, every=1)
    pt = PeriodicTask.objects.create(
        name="notify of starting soon",
        interval = minute_schedule, 
        task = "movies.tasks.notify_of_starting_soon"
    )
