from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/edit/', EditView.as_view(), name='edit'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='edit'),
]
