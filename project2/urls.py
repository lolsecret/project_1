"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from univers import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UniverListView.as_view(), name='univer'),
    path('univer/<int:pk>', views.UniverDetailView.as_view(), name='univer-detail'),
    path('univer/<int:pk>/delete', views.UniverDelete.as_view(), name="univer-delete"),
    path('univer/create', views.UniverCreate.as_view(), name="univer-create"),

    #path('chair/<int:pk>', views.ChairListView.as_view(), name='chair'),
    path('chair/create', views.ChairCreate.as_view(), name='chair-create'),
    path('chair/<int:pk>', views.ChairDetailView.as_view(), name='chair-detail'),
    path('chair/<int:pk>/delete', views.ChairDelete.as_view(), name='chair-delete'),

    path('spec/create', views.SpecCreate.as_view(), name='spec-create'),
    path('spec/<int:pk>', views.SpecDetailView.as_view(), name='spec-detail'),
    path('spec/<int:pk>/delete', views.SpecDelete.as_view(), name='spec-delete'),

    path('group/create', views.GroupSpecCreate.as_view(), name='group-create'),
    path('group/<int:pk>', views.GroupSpecDetailView.as_view(), name='group-detail'),
    path('group/<int:pk>/delete', views.GroupSpecDelete.as_view(), name='group-delete'),
    path('', include('univers.urls')),
    path('', include('authorizations.urls')),

    #include api
    path('api', include('api.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]