from django.db import models


class JPHModel(models.Model):
    userId = models.IntegerField(null=False)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=240)
    body = models.TextField()
    update_date = models.DateTimeField(null=True)

    objects = models.Manager()

    class Meta:
        ordering = ["id"]
