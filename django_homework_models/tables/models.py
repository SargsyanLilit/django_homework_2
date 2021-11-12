from django.db import models


class Film(models.Model):
    name = models.TextField(max_length=100)
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField()
    status = models.IntegerField(choices=((0, "New"), (1, "Old")))

    def __str__(self):
        return self.name

