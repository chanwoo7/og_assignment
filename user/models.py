from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User: 유저 정보 모델
    """

    is_artist = models.BooleanField(default=False)  # 작가 여부
    contact_number = models.CharField(max_length=15, blank=True, null=True)  # 연락처

    def __str__(self):
        return self.username
