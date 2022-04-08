from django.urls import path,include
from .import views

from .views import (
    Dashboard_Page,
)
urlpatterns = [
    path('', Dashboard_Page.as_view(), name = 'dashboard'),
]
