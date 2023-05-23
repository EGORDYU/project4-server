from django.contrib.auth.models import User
from django.db import models

class BuildOrder(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    buildorder = models.TextField(default="")  # Add a default value here
    matchup = models.CharField(max_length=120, default="")  # And here

    def __str__(self):
        return self.title



class Comment(models.Model):
    build_order = models.ForeignKey(BuildOrder, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment by {self.user.username} on {self.build_order.title}'
