from rest_framework import serializers
from .models import Artwork


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ['title', 'price', 'size']

    def validate_title(self, value):
        # 제목이 1~64자 이내인지 검사
        if len(value) > 64:
            raise serializers.ValidationError("제목은 64자 이내여야 합니다.")
        return value

    def validate_price(self, value):
        # 가격이 0 이상의 값인지 검사
        if value < 0:
            raise serializers.ValidationError("가격은 0 이상이어야 합니다.")
        return value

    def validate_size(self, value):
        # 호수가 1 이상 500 이하인지 검사
        if value < 1 or value > 500:
            raise serializers.ValidationError("호수는 1 이상 500 이하이어야 합니다.")
        return value
