from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=250)
    icon = models.FileField(upload_to='course_icons')
    mini_description = models.TextField()

