from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    description = models.TextField(default="")
    content = models.TextField(blank=False, default="")
    author = models.CharField(max_length=200, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    post_status = models.IntegerField(choices=STATUS, default=0)
