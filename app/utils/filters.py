from rest_framework.filters import BaseFilterBackend


class OwnerFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user

        if user.is_superuser:
            return queryset

        if user.is_anonymous:
            return queryset.none()

        return queryset.filter(owner=request.user)
