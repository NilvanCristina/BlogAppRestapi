from django.contrib.auth.models import User
from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    description = models.TextField(default="")
    content = models.TextField(blank=False, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    post_status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title
