from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('anime_app.urls')), 
    # re_path(r'^.*$'),
]