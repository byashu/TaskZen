from django.urls import path
from . import views

urlpatterns = [
    # --- 1. CORE PAGES ---
    path('', views.index_view, name='home'),
    path('taskboard/', views.taskboard_view, name='taskboard'),

    # --- 2. SMART FEATURES ---
    path('productivity/', views.productivity_stats, name='productivity_stats'),
    path('summary/', views.task_summary, name='task_summary'),

    # --- 3. TASK CRUD ---
    path('add/', views.add_task, name='add_task'),
    path('detail/<int:pk>/', views.task_detail, name='task_detail'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('mark-done/<int:pk>/', views.mark_done, name='mark_done'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),

    # --- 4. SUBTASKS ---
    path('subtask/add/<int:pk>/', views.add_subtask, name='add_subtask'),
    path('subtask/toggle/<int:pk>/', views.toggle_subtask, name='toggle_subtask'),
    path('subtask/delete/<int:pk>/', views.delete_subtask, name='delete_subtask'),

    # --- 5. CATEGORIES ---
    path('categories/', views.manage_categories, name='manage_categories'),

    # --- 6. EXPORT ---
    path('export/excel/', views.export_excel, name='export_excel'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),

    # --- 7. AUTHENTICATION ---
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
