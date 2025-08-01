from django.urls import path
from todo_list import views
from django.contrib.auth.views import LogoutView

app_name = "todo"

urlpatterns = [
    path('home', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('todo/', views.todo, name='todo'),
    path('delete/<int:srno>/', views.delete_task, name='delete_task'),
    path('edit/<int:srno>/', views.edit_task, name='edit_task'),
    path('logout/', LogoutView.as_view(next_page='todo:login'), name='logout'),
]
