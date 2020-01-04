from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('administracion/', include('administracion.urls', namespace="administracion")),
    path('admin/', admin.site.urls),
]