from django.urls import path,include
from .import views

from .views import (
    Order_Document_Page,
    Order_Document_Create,
    Order_Document_Create_AJAXView,
    Order_Document_Update,
    Order_Document_Update_AJAXView,
    Order_Document_Update_Save_AJAXView,
    Order_Document_Table_AJAXView,
    # Order_Document_Print,
)
# 127.0.0.1:8000/outgoing_document/
urlpatterns = [
    path('', Order_Document_Page.as_view(), name = 'order_document'),
    path('create', Order_Document_Create.as_view(), name = 'order_document_create'),
    path('api/create', Order_Document_Create_AJAXView.as_view(), name = 'order_document_create_api'),
    path('update/<uuid:pk>', Order_Document_Update.as_view(), name = 'order_document_update'),
    path('api/update/', Order_Document_Update_AJAXView.as_view(), name = 'order_document_update_api'),
    path('api/update/save/<uuid:pk>', Order_Document_Update_Save_AJAXView.as_view(), name = 'order_document_update_save_api'),
    path('api/table', Order_Document_Table_AJAXView.as_view(), name = 'order_document_table_api'),
    # path('reports/print/<int:pk>', Order_Document_Print.as_view(), name = 'order_document_print'),

]
