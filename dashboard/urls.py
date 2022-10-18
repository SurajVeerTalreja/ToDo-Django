from django.urls import path
from . import views

urlpatterns = [ 
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('entry/', views.ToDoCreate.as_view(), name='entry'),
    path('todo_list/', views.ToDoListView.as_view(), name='todo_list'),
    path('detail_list/<int:pk>', views.DetailListView.as_view(), name='detail_list'),
    path('update_entry/<int:pk>', views.UpdateList.as_view(), name='update_list'),
    path('delete_entry/<int:pk>', views.DeleteEntry.as_view(), name='delete_list'),
]