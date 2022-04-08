from django.urls import path,include
from .import views

from .views import (
    Security_Page,
    Security_AJAXView
)
urlpatterns = [
    path('', Security_Page.as_view(), name = 'security'),
    path('api', Security_AJAXView.as_view(), name = 'api_security'),
]
