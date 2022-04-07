from django.urls import path,include
from .import views

from .views import (
    Home,
    Security_Page,
    Security_AJAXView,
)

urlpatterns = [
    path('', Home.as_view(), name = 'dashboard'),
    path('document/', include('application.page_incoming_document.urls')),
    path('outgoing/', include('application.page_outgoing_document.urls')),
    path('order/', include('application.page_order_document.urls')),
    # path('category/', include('application.page_category.urls')),
    path('year/', include('application.page_year.urls')),
    path('security/', Security_Page.as_view(), name = 'security'),
    path('api/security', Security_AJAXView.as_view(), name = 'api_security'),
]
