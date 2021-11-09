from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(max_length=200, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.email
