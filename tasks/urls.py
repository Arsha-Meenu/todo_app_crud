from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='list-tasks'),
    path('update_task/<str:pk>/',views.UpdateTask,name="update-task"),
    path('delete_task/<str:pk>/',views.DeleteTask,name="delete-task"),
]
