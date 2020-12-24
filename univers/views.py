from .models import Univer, Chair, Specialization, GroupSpec
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
# D R F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from users.models import User

# Create your views here.
class UniverDetailView(generic.DetailView):
    model = Univer

class UniverListView(generic.ListView):
    model = Univer


class UniverDelete(DeleteView):
    model = Univer
    success_url = reverse_lazy('univer')


class UniverCreate(CreateView):
    model = Univer
    fields = '__all__'


# CHAIR
class ChairDetailView(generic.DetailView):
    model = Chair


class ChairCreate(CreateView):
    model = Chair
    fields = '__all__'


class ChairDelete(DeleteView):
    model = Univer
    success_url = reverse_lazy('/')


# SPEC
class SpecCreate(CreateView):
    model = Specialization
    fields = '__all__'


class SpecDetailView(generic.DetailView):
    model = Specialization


class SpecDelete(DeleteView):
    model = Specialization
    success_url = reverse_lazy('/')


# GROUP SPEC
class GroupSpecCreate(CreateView):
    model = GroupSpec
    fields = '__all__'


class GroupSpecDetailView(generic.DetailView):
    model = GroupSpec


class GroupSpecDelete(DeleteView):
    model = GroupSpec
    success_url = reverse_lazy('/')


#DRF
class ListUsers(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        print(self,request)
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)