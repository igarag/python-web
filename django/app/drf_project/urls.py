from django.contrib import admin
from django.urls import path, include

from .views import ping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', ping, name="ping"),
    path("", include("movies.urls")),
]
