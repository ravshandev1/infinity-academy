from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
