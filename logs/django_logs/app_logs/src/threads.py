from threading import Thread
from django.utils import timezone
from .kafka_consumer import balanced_consumer
from ..models import LogRecord
from concurrent.futures import ThreadPoolExecutor


# def waiting_messages():
#     for message in balanced_consumer:
#         if message is not None:
#             print(message.offset, message.value.decode("utf-8"))
#             record = LogRecord(timestamp=timezone.now(), type_of_sync=message.value.decode("utf-8"))
#             record.save()


# # thread_log = Thread(target=waiting_messages())
#
# def thread_log():
#     with ThreadPoolExecutor(max_workers=1) as executor:
#         executor.map(waiting_messages, range(1))


class CreateLogsThread(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        try:
            print('Thread execution started')
            while True:
                for message in balanced_consumer:
                    if message is not None:
                        print(message.offset, message.value.decode("utf-8"))
                        record = LogRecord(timestamp=timezone.now(), type_of_sync=message.value.decode("utf-8"))
                        record.save()
        except Exception as e:
            print(e)
