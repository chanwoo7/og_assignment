from django.db import models
from artist.models import Artist
from artwork.models import Artwork


class Exhibition(models.Model):
    """
    Exhibition: 전시 정보 모델
    """

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)  # 작가와 1:N 관계
    title = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    artworks = models.ManyToManyField(Artwork)  # 전시에 여러 작품이 포함될 수 있음

    def __str__(self):
        return f"{self.title} by {self.artist.name}"