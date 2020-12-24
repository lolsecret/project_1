from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()

urlpatterns=[
    path('', include(router.urls)),
    path('univer', views.UniverView.as_view(), name='univer-detail'),
    path('chair', views.ChairView.as_view(), name='chair-detail')
]