import re

from rest_framework import serializers
from .models import ArtistApplication
from datetime import date


class ArtistApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistApplication
        fields = ['name', 'gender', 'birth_date', 'email', 'contact_number']

    def validate_name(self, value):
        # 이름이 1~16자의 한글 또는 영문자인지 검사
        if not re.match(r"^[a-zA-Z가-힣]{1,16}$", value):
            raise serializers.ValidationError("이름은 1~16자의 한글 또는 영문자여야 합니다.")
        return value

    def validate_birth_date(self, value):
        # 생년월일이 미래 날짜가 아닌지 검사
        if value > date.today():
            raise serializers.ValidationError("생년월일은 현재 날짜보다 이전이어야 합니다.")
        return value

    def validate_gender(self, value):
        # 성별이 'M' 또는 'F'인지 검사
        if value not in ['M', 'F']:
            raise serializers.ValidationError("성별은 'M' 또는 'F'만 가능합니다.")
        return value

    def validate_email(self, value):
        # 이메일 형식이 올바른지 검사
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("올바른 이메일 주소를 입력해주세요.")
        return value

    def validate_contact_number(self, value):
        # 연락처가 010-XXXX-XXXX 형식인지 검사
        if not re.match(r"^010-\d{4}-\d{4}$", value):
            raise serializers.ValidationError("연락처는 '010-XXXX-XXXX' 형식이어야 합니다.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user

        # 신청자가 이미 대기 중인 신청이 있는지 체크
        if ArtistApplication.objects.filter(applicant=user, status='Pending').exists():
            raise serializers.ValidationError({"non_field_errors": ["이미 대기 중인 신청이 존재합니다."]})

        return ArtistApplication.objects.create(
            applicant=user,
            name=validated_data['name'],
            gender=validated_data['gender'],
            birth_date=validated_data['birth_date'],
            email=validated_data['email'],
            contact_number=validated_data['contact_number'],
        )
