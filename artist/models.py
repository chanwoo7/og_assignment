from django.db import models
from user.models import User

# 성별
GENDER_CHOICES = [
    ('M', '남성'),
    ('F', '여성')
]

# 신청 상태
STATUS_CHOICES = [
    ('Pending', '대기 중'),
    ('Approved', '승인됨'),
    ('Rejected', '반려됨')
]


class Artist(models.Model):
    """
    Artist: 작가 정보 모델
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 1:1 관계로 User와 연결
    name = models.CharField(max_length=64)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField()
    contact_number = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class ArtistApplication(models.Model):
    """
    ArtistApplication: 작가 등록 신청 내역 모델
    """

    applicant = models.ForeignKey(User, on_delete=models.CASCADE)  # 신청자
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    # 신청 시점의 작가 정보 저장
    name = models.CharField(max_length=64)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    email = models.EmailField()
    contact_number = models.CharField(max_length=13)

    def __str__(self):
        return f"{self.name} - {self.status}"
