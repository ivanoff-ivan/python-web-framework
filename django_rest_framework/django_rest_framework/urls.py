from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('django_rest_framework.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('django_rest_framework.web.urls')),
]
