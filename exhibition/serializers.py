from rest_framework import serializers
from exhibition.models import Exhibition
from artwork.models import Artwork


class ExhibitionSerializer(serializers.ModelSerializer):
    artworks = serializers.PrimaryKeyRelatedField(queryset=Artwork.objects.all(), many=True)

    class Meta:
        model = Exhibition
        fields = ['title', 'start_date', 'end_date', 'artworks']

    def validate_title(self, value):
        # 제목이 64자 이내인지 검사
        if len(value) > 64:
            raise serializers.ValidationError("제목은 64자 이내여야 합니다.")
        return value

    def validate(self, data):
        # 시작일과 종료일이 올바른지 확인
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("시작일은 종료일보다 앞서야 합니다.")
        return data
