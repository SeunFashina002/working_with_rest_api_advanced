from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class IsStaffUserPermissionMixin():
    permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]

class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = True
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user

        qs = super().get_queryset(*args, **kwargs)

        if self.allow_staff_view and user.is_staff: #--> only staff and admin users can see all products
            return qs
        return qs.filter(**lookup_data)