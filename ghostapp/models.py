from django.db import models
from django.utils import timezone

# Create your models here.
"""
One model to represent both boasts and roasts

-Boolean to tell whether it's a boast or a roast
-CharField to put the content of the post in
-IntegerField for up votes
-IntegerField for down votes
-DateTimeField for submission time
"""

class VoteChoice(models.Model):
    choice = models.BooleanField(default=False)
    text = models.CharField(max_length=280)
    time = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.text