from celery import shared_task


@shared_task
def habit_track(habit_id):
    """
    Таск Celery для напоминания о выполнении привычки
    """
    remind_of_habit(habit_id)