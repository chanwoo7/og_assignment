from django.db import models
from artist.models import Artist


class Artwork(models.Model):
    """
    Artwork: 작품 정보 모델
    """

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # Artist와 1:N 관계
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.PositiveIntegerField()  # 호수, 1 이상 500 이하의 값

    def __str__(self):
        return f"{self.title} by {self.artist.name}"
