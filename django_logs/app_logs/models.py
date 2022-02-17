from django.db import models


class LogRecord(models.Model):
    timestamp = models.DateTimeField('Timestamp', null=False)
    type_of_sync = models.CharField('Type of sync', max_length=100, null=False)
