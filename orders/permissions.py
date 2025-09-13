from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedAndManagerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        
        print("Permission check triggered")
        print("User:", request.user)
        print("Authenticated:", request.user.is_authenticated)
        print("Method:", request.method)
        print("Role:", getattr(request.user, 'role', 'N/A'))

        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS or request.method == 'POST':
            return True
        return request.user.role == 'manager'

class IsManagerOrOwner(BasePermission):
    """
    Managers can view/edit/delete any order.
    Customers can only view/edit/delete their own orders.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'manager':
            return True
        return obj.customer == request.user

