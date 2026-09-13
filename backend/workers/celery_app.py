from celery import Celery
from ..config import settings

celery_app = Celery(
    "jaldhara_worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["backend.workers.tasks"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=True,
)
