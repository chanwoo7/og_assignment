from rest_framework.permissions import BasePermission


class IsArtist(BasePermission):
    """
    커스텀 권한: 유저가 작가(is_artist=True)인지 확인
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_artist)


class IsNotArtist(BasePermission):
    """
    커스텀 권한: 유저가 작가가 아닌 유저(is_artist=False)인지 확인
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and not request.user.is_artist)
