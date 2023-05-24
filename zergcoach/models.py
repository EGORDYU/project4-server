from django.contrib.auth.models import User
from django.db import models
from markdown_it import MarkdownIt

md = MarkdownIt()


class BuildOrder(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    buildorder = models.TextField(default="")
    matchup = models.CharField(max_length=120, default="")
    imgur_link = models.CharField(max_length=255, null=True, blank=True)  # Add imgur_link field

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.buildorder = md.render(self.buildorder)  # Format buildorder content as Markdown
        super().save(*args, **kwargs)



class Comment(models.Model):
    build_order = models.ForeignKey(BuildOrder, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'Comment by {self.user.username} on {self.build_order.title}'
