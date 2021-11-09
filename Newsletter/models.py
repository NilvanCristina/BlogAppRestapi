from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(max_length=200, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.email
