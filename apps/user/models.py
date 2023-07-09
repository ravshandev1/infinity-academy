from django.db import models


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Team(models.Model):
    name = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)
    image = models.FileField(upload_to='team')
    stata = models.CharField(max_length=250)
    stata_description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Team'
        verbose_name = 'Team'


class About(models.Model):
    pass
