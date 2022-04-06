from django.urls import path,include
from .import views

from .views import (
    Document_Page,
    Document_Create,
    Document_Create_AJAXView,
    Document_Update,
    Document_Update_AJAXView,
    Document_Update_Save_AJAXView,
    Document_Table_AJAXView,
    # Document_Print,
)
# 127.0.0.1:8000/document/
urlpatterns = [
    path('', Document_Page.as_view(), name = 'document'),
    path('create', Document_Create.as_view(), name = 'document_create'),
    path('api/create', Document_Create_AJAXView.as_view(), name = 'document_create_api'),
    path('update/<uuid:pk>', Document_Update.as_view(), name = 'document_update'),
    path('api/update/', Document_Update_AJAXView.as_view(), name = 'document_update_api'),
    path('api/update/save/<uuid:pk>', Document_Update_Save_AJAXView.as_view(), name = 'document_update_save_api'),
    path('api/table', Document_Table_AJAXView.as_view(), name = 'document_table_api'),
    # path('reports/print/<int:pk>', Document_Print.as_view(), name = 'document_print'),

]
