from django.urls import path, include
from . import views

urlpatterns=[
    path('univer', views.UniverView.as_view(), name='univer-detail'),
    path('chair', views.ChairView.as_view(), name='chair-detail')
]