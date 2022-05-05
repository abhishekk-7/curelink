from django.db import models
from content.models import ContentModel
# Create your models here.


class UserModel(models.Model):
    email = models.EmailField(max_length=100)
    topic = models.ForeignKey(
        ContentModel, to_field="topic", on_delete=models.CASCADE)

    def __str__(self):
        return self.email
