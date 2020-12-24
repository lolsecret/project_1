from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, permissions
from rest_framework.generics import ListAPIView
from univers.models import Univer, Chair
from .seralizers import UniverSerializers, ChairSerializers, SpecializationSerializers
from .permissions import IsRector, IsHeadOfDep
from rest_condition import Or

class UniverView(ListAPIView):
    queryset = Univer.objects.all()
    serializer_class = UniverSerializers
    permission_classes = (Or(permissions.IsAdminUser, IsRector),)

    def filter_queryset(self, queryset):
        if self.request.user.role == 'r':
            queryset = queryset.filter(rector_id=self.request.user)
        return queryset

class ChairView(ListAPIView):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializers
    permission_classes = (Or(IsRector, IsHeadOfDep),)

    def filter_queryset(self, queryset):
        univer = Univer.objects.all()
        univer = univer.filter(rector_id=self.request.user)
        univer_id = [univer_id.id for univer_id in univer]

        if self.request.user.role == 'hod':
            queryset = queryset.filter(head_of_dep_id=self.request.user)
        return queryset.filter(univer_id = univer_id[0])
