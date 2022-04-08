from django.urls import path,include
from .import views

urlpatterns = [
    path('', include('application.page_dashboard.urls')),
    path('document/', include('application.page_incoming_document.urls')),
    path('outgoing/', include('application.page_outgoing_document.urls')),
    path('order/', include('application.page_order_document.urls')),
    path('year/', include('application.page_year.urls')),
    path('security/', include('application.page_security.urls')),

]
