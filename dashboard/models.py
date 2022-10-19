from django.db import models
from django.utils.timezone import datetime


class Storage(models.Model):
    user = models.CharField(max_length=225)
    file_name = models.CharField(max_length=225)
    description = models.CharField(max_length=225, blank=True)
    access_time = models.DateTimeField(default=datetime.now())
    file = models.FileField(upload_to='personalFiles')

    def delete(self, using=None, keep_parents=False):
        self.file.storage.delete(self.file.name)
        super().delete()
