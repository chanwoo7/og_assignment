from django.contrib.auth import get_user_model
from rest_framework import serializers


# 비밀번호 유효성 검사
def validate_password(password):
    # 1. 길이 (8자 이상 16자 이하)
    if len(password) < 8 or len(password) > 16:
        raise serializers.ValidationError("비밀번호는 8자 이상이어야 합니다.")

    # 2. 숫자 포함 여부
    if not any(char.isdigit() for char in password):
        raise serializers.ValidationError("비밀번호는 적어도 1개의 숫자를 포함해야 합니다.")

    # 3. 영문자 포함 여부
    if not any(char.isalpha() for char in password):
        raise serializers.ValidationError("비밀번호는 적어도 1개의 영문자를 포함해야 합니다.")

    # 4. 특수문자 포함 여부
    if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>/?' for char in password):
        raise serializers.ValidationError("비밀번호는 적어도 1개의 특수문자를 포함해야 합니다.")

    return password


class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다."})

        # 비밀번호 유효성 검사 호출
        validate_password(attrs['password'])

        return attrs

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
