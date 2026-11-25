
from django.contrib import admin
from django.urls import path, include
from fall2026 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', include('fall2026.urls')),
    path('',views.home, name = 'home'),
]
