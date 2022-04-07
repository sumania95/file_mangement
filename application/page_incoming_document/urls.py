from django.urls import path,include
from .import views

from .views import (
    Incoming_Document_Page,
    Incoming_Document_Create,
    Incoming_Document_Create_AJAXView,
    Incoming_Document_Update,
    Incoming_Document_Update_AJAXView,
    Incoming_Document_Update_Save_AJAXView,
    Incoming_Document_Table_AJAXView,
    # Incoming_Document_Print,
)
# 127.0.0.1:8000/incoming_document/
urlpatterns = [
    path('', Incoming_Document_Page.as_view(), name = 'incoming_document'),
    path('create', Incoming_Document_Create.as_view(), name = 'incoming_document_create'),
    path('api/create', Incoming_Document_Create_AJAXView.as_view(), name = 'incoming_document_create_api'),
    path('update/<uuid:pk>', Incoming_Document_Update.as_view(), name = 'incoming_document_update'),
    path('api/update/', Incoming_Document_Update_AJAXView.as_view(), name = 'incoming_document_update_api'),
    path('api/update/save/<uuid:pk>', Incoming_Document_Update_Save_AJAXView.as_view(), name = 'incoming_document_update_save_api'),
    path('api/table', Incoming_Document_Table_AJAXView.as_view(), name = 'incoming_document_table_api'),
    # path('reports/print/<int:pk>', Incoming_Document_Print.as_view(), name = 'incoming_document_print'),

]
