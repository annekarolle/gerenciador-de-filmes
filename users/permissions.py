from rest_framework import permissions
from rest_framework.views import Request, View

from users.models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:       

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return False

class Authenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:       

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return True

        return False

class IsProfileOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, user: User) -> bool:        
        if user.email == request.user.email or request.user.is_superuser:
            return True
        return False
    
    def has_permission(self, request: Request, view: View) -> bool:      
        
        if request.user.is_authenticated: 
            return True

        return False

       