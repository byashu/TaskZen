from django.urls import path
from . import views

urlpatterns = [
    # Main Navigation
    path('', views.index_view, name='home'), 
    
    # Taskboard handles both list view, search, and sorting via GET parameters
    path('taskboard/', views.taskboard_view, name='taskboard'),
    
    # Smart Features (Productivity and Summary)
    path('productivity/', views.productivity_stats, name='productivity_stats'),
    path('summary/', views.task_summary, name='task_summary'),
    
    # Task Operations (CRUD)
    path('add/', views.add_task, name='add_task'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('mark-done/<int:pk>/', views.mark_done, name='mark_done'),
    
    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
]