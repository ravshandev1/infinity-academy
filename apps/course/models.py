from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=250)
    icon = models.FileField(upload_to='course_icons')
    link = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
