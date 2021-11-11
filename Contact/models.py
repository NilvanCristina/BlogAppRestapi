from django.db import models

SUBJECT = (
    (0, "Collaboration"),
    (1, "Meeting"),
    (2, "Consultancy"),
    (3, "Gratitude")
)


class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    subject = models.IntegerField(choices=SUBJECT, default=3)
    message = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.email
