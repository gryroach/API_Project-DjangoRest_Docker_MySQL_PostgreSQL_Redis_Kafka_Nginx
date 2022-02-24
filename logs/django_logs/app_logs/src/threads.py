from threading import Thread
from django.utils import timezone
from .kafka_consumer import balanced_consumer
from ..models import LogRecord


def waiting_messages():
    for message in balanced_consumer:
        if message is not None:
            print(message.offset, message.value.decode("utf-8"))
            record = LogRecord(timestamp=timezone.now(), type_of_sync=message.value.decode("utf-8"))
            record.save()


# thread_log = Thread(target=waiting_messages())
