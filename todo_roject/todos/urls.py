from django.urls import path
from . import htmlx_views

urlpatterns = [

    # HTMX-powered views
    path('', htmlx_views.todo_list, name='todo_list'),
    path('create/', htmlx_views.todo_create, name='todo_create'),
    path('update/<int:pk>/', htmlx_views.todo_update, name='todo_update'),
    path('delete/<int:pk>/', htmlx_views.todo_delete, name='todo_delete'),
]