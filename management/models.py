from django.db import models
from artist.models import ArtistApplication


class AdminLog(models.Model):
    """
    AdminLog: 관리자가 어떤 신청을 어떻게 처리했는지 기록하는 모델
    """

    action = models.CharField(max_length=64)
    artist_application = models.ForeignKey(ArtistApplication, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - {self.artist_application.name}"
