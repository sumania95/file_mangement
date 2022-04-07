from django.urls import path,include
from .import views

from .views import (
    Outgoing_Document_Page,
    Outgoing_Document_Create,
    Outgoing_Document_Create_AJAXView,
    Outgoing_Document_Update,
    Outgoing_Document_Update_AJAXView,
    Outgoing_Document_Update_Save_AJAXView,
    Outgoing_Document_Table_AJAXView,
    # Outgoing_Document_Print,
)
# 127.0.0.1:8000/outgoing_document/
urlpatterns = [
    path('', Outgoing_Document_Page.as_view(), name = 'outgoing_document'),
    path('create', Outgoing_Document_Create.as_view(), name = 'outgoing_document_create'),
    path('api/create', Outgoing_Document_Create_AJAXView.as_view(), name = 'outgoing_document_create_api'),
    path('update/<uuid:pk>', Outgoing_Document_Update.as_view(), name = 'outgoing_document_update'),
    path('api/update/', Outgoing_Document_Update_AJAXView.as_view(), name = 'outgoing_document_update_api'),
    path('api/update/save/<uuid:pk>', Outgoing_Document_Update_Save_AJAXView.as_view(), name = 'outgoing_document_update_save_api'),
    path('api/table', Outgoing_Document_Table_AJAXView.as_view(), name = 'outgoing_document_table_api'),
    # path('reports/print/<int:pk>', Outgoing_Document_Print.as_view(), name = 'outgoing_document_print'),

]
