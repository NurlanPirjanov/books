from django.urls import path
from .views import *

urlpatterns = [
    path('new/', BookCreateView.as_view(), name='book_new'),
    path('', BookList, name='list'),
    path('export/', BookExportView.as_view(), name='book_export'),
    path('export_xls/', export_excel_xls, name='book_export_xls'),
    path('search/', search.as_view(), name="search"),
]