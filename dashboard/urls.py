from django.urls import path

from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('upload', views.CreateFile.as_view(), name='upload'),
    path('view_files', views.ViewFile.as_view(), name='view_files'),
    path('delete_file/<int:pk>', views.DeleteFile.as_view(), name='delete_file')
]
