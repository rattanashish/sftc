from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class user_bac_video(models.Model):
    bac_level = models.FloatField(null=True, blank=True)
    user_video = models.FileField(upload_to='user_videos/')
    user = models.ForeignKey(User,related_name='user_bac', on_delete=models.CASCADE,):
)
    timestamp = models.TimeField(auto_now_add=True)


