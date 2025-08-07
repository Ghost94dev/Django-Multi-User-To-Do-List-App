from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from todo_list.models import TODOO
from datetime import timedelta

@shared_task
def send_reminder(srno):
    todo = TODOO.objects.get(srno=srno)
    send_mail(
        f"Reminder: {todo.title}",
        f"Your task is due at {todo.due_date}",
        'from@example.com',
        [todo.user.email]
    )