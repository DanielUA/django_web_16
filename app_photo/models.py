from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size
    if filesize > 1_000_000:
        raise ValidationError("Max file size is 1mb")
    return value

class Pictures(models.Model):
    description = models.CharField(max_length=300)
    path = models.ImageField(upload_to='images', validators=[validate_file_size])
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
