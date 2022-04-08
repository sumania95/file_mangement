from django.urls import path,include
from .import views

from .views import (
    Ordinance_Resolution_Document_Page,
    Ordinance_Resolution_Document_Create,
    Ordinance_Resolution_Document_Create_AJAXView,
    Ordinance_Resolution_Document_Update,
    Ordinance_Resolution_Document_Update_AJAXView,
    Ordinance_Resolution_Document_Update_Save_AJAXView,
    Ordinance_Resolution_Document_Table_AJAXView,
)
urlpatterns = [
    path('', Ordinance_Resolution_Document_Page.as_view(), name = 'ordinance_resolution_document'),
    path('create', Ordinance_Resolution_Document_Create.as_view(), name = 'ordinance_resolution_document_create'),
    path('api/create', Ordinance_Resolution_Document_Create_AJAXView.as_view(), name = 'ordinance_resolution_document_create_api'),
    path('update/<uuid:pk>', Ordinance_Resolution_Document_Update.as_view(), name = 'ordinance_resolution_document_update'),
    path('api/update/', Ordinance_Resolution_Document_Update_AJAXView.as_view(), name = 'ordinance_resolution_document_update_api'),
    path('api/update/save/<uuid:pk>', Ordinance_Resolution_Document_Update_Save_AJAXView.as_view(), name = 'ordinance_resolution_document_update_save_api'),
    path('api/table', Ordinance_Resolution_Document_Table_AJAXView.as_view(), name = 'ordinance_resolution_document_table_api'),

]
