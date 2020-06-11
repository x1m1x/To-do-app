from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('to_do/', include('to_do_list.urls')),
    path('admin/', admin.site.urls),
]
