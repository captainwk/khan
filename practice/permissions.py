from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # 모든 요청에 ​​대해 읽기 권한이 허용됩니다.
        # 그래서 우리는 항상 GET, HEAD 또는 OPTIONS 요청을 허용합니다.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 스 니펫 소유자에게만 허용됩니다.
        return obj.owner == request.user