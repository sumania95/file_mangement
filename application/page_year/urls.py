from django.urls import path,include
from .import views

from .views import (
    Year_Page,
    Year_Create,
    Year_Create_AJAXView,
    Year_Update,
    Year_Update_AJAXView,
    Year_Update_Save_AJAXView,
    Year_Table_AJAXView,
    # Year_Print,
)
# 127.0.0.1:8000/year/
urlpatterns = [
    path('', Year_Page.as_view(), name = 'year'),
    path('create', Year_Create.as_view(), name = 'year_create'),
    path('api/create', Year_Create_AJAXView.as_view(), name = 'year_create_api'),
    path('update/<uuid:pk>', Year_Update.as_view(), name = 'year_update'),
    path('api/update/', Year_Update_AJAXView.as_view(), name = 'year_update_api'),
    path('api/update/save/<uuid:pk>', Year_Update_Save_AJAXView.as_view(), name = 'year_update_save_api'),
    path('api/table', Year_Table_AJAXView.as_view(), name = 'year_table_api'),
    # path('reports/print/<int:pk>', Year_Print.as_view(), name = 'year_print'),

]
