from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from todo import views

urlpatterns = [
    path('', RedirectView.as_view(url='todo/')),  # Redirect the root URL to 'todo/'
    path('todo/', views.todo_list, name="todo_list"),
    path('todo/create_todo', views.create_todo, name="create_todo"),
    path('todo/complete/<int:todo_id>/', views.complete_todo, name='complete_todo'),
    path('todo/delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path("admin/", admin.site.urls),
]