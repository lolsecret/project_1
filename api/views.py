from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from univers.models import Univer, Chair
from .seralizers import UniverSerializers, ChairSerializers
from .permissions import IsRector, IsHeadOfDep
from rest_condition import Or


class UniverView(ListAPIView):
    queryset = Univer.objects.all()
    serializer_class = UniverSerializers
    permission_classes = (Or(permissions.IsAdminUser, IsRector),)

    def filter_queryset(self, queryset):
        if self.request.user.RoleTypes.RECTOR:
            queryset = queryset.filter(rector_id=self.request.user)
        return queryset


from users.models import RoleTypes

class ChairView(ListAPIView):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializers
    permission_classes = (Or(IsRector, IsHeadOfDep),)

    def filter_queryset(self, queryset):
        user = self.request.user

        if user.role == RoleTypes.RECTOR:
            return self.queryset.filter(univer=user.univer)
        elif user.role == RoleTypes.HEAD_OF_DEP:
            return queryset.filter(head_of_dep_id=self.request.user)
