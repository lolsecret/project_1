from rest_framework import permissions
from rest_framework.generics import ListAPIView
from univers.models import Univer, Chair
from .seralizers import UniverSerializers, ChairSerializers
from .permissions import IsRector, IsHeadOfDep
from rest_condition import Or


class UniverView(ListAPIView):
    queryset = Univer.objects.all()
    serializer_class = UniverSerializers
    permission_classes = (Or(permissions.IsAdminUser, IsRector),)

    def filter_queryset(self, queryset):
        if self.request.user.is_rector:
            queryset = queryset.filter(rector_id=self.request.user)
        return queryset


class ChairView(ListAPIView):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializers
    permission_classes = (Or(IsRector, IsHeadOfDep),)

    def filter_queryset(self, queryset):
        univer = UniverView.queryset.filter(rector_id=self.request.user)

        if self.request.user.is_hod:
            return queryset.filter(head_of_dep_id=self.request.user)
        return queryset.filter(univer_id = univer.first().id)
