from rest_framework.permissions import BasePermission


class IsHuman(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user == obj.human:
            return True
        return False


#
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_superuser or obj.user.id == request.user.id
