from django.urls import path
from . import views

urlpatterns = [
    # --- 1. CORE PAGES ---
    path('', views.index_view, name='home'), 
    
    # Taskboard handles list view, search, and sorting via GET parameters
    path('taskboard/', views.taskboard_view, name='taskboard'),
    
    # --- 2. SMART FEATURES (CHARTS & ANALYTICS) ---
    # These match the functions providing data for your summary and productivity charts
    path('productivity/', views.productivity_stats, name='productivity_stats'),
    path('summary/', views.task_summary, name='task_summary'),
    
    # --- 3. TASK OPERATIONS (CRUD) ---
    path('add/', views.add_task, name='add_task'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('mark-done/<int:pk>/', views.mark_done, name='mark_done'),
    
    # --- 4. AUTHENTICATION ---
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
]