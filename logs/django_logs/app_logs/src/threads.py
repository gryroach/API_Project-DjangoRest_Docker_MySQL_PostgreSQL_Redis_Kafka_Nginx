from threading import Thread
from django.utils import timezone
from .kafka_consumer import balanced_consumer
from ..models import LogRecord


class CreateLogsThread(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        try:
            print('Thread of logging started')
            while True:
                for message in balanced_consumer:
                    if message is not None:
                        record = LogRecord(timestamp=timezone.now(), type_of_sync=message.value.decode("utf-8"))
                        record.save()
                        print(f"Offset {message.offset} {message.value.decode('utf-8')} added in database")
        except Exception as e:
            print(e)
