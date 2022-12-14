from django.db import models


class Resize(models.Model):
    image_to_resize = models.ImageField()
    image_id_from_request = models.IntegerField()
    user_id_from_request = models.IntegerField()


class ErrorLog(models.Model):
    image_id : models.IntegerField()
    error_date = models.DateTimeField(auto_now=True)