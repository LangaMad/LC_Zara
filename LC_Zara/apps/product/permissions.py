from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS 



class IsOwnerOrReadOnly(permissions.BasePermission):
    def  has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff
    

class isAuthenticatedOrIsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff or request.user