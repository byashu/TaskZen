from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Task

# --- 1. CORE PAGES ---

def index_view(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def taskboard_view(request):
    # 1. Get initial tasks for the logged-in user
    tasks = Task.objects.filter(user=request.user)

    # 2. Handle Search Logic
    search_query = request.GET.get('search')
    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )

    # 3. Handle Sorting Logic
    sort_by = request.GET.get('sort')
    if sort_by == 'priority':
        # Sorting by priority (High -> Medium -> Low)
        tasks = tasks.order_by('priority') 
    elif sort_by == 'due':
        tasks = tasks.order_by('due_date')
    else:
        # Default: Newest first
        tasks = tasks.order_by('-created_at')

    context = {
        'tasks': tasks,
        'search_query': search_query 
    }
    return render(request, 'taskboard.html', context)

@login_required(login_url='login')
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'detail.html', {'task': task})

# --- 2. SMART FEATURES ---

@login_required(login_url='login')
def productivity_stats(request):
    tasks = Task.objects.filter(user=request.user)
    total_tasks = tasks.count()
    
    # Calculate counts for different priorities
    high_priority = tasks.filter(priority='High').count()
    medium_priority = tasks.filter(priority='Medium').count()
    low_priority = tasks.filter(priority='Low').count()
    
    # Calculate completed vs pending (assuming you have a 'completed' boolean field)
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()
    
    context = {
        'total': total_tasks,
        'high': high_priority,
        'medium': medium_priority,
        'low': low_priority,
        'completed': completed_tasks,
        'pending': pending_tasks,
    }
    return render(request, 'productivity.html', context)

@login_required(login_url='login')
def task_summary(request):
    tasks = Task.objects.filter(user=request.user).order_by('due_date')
    return render(request, 'summary.html', {'tasks': tasks})

# --- 3. TASK CRUD OPERATIONS ---

@login_required(login_url='login')
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        
        Task.objects.create(
            user=request.user,
            title=title, 
            description=description, 
            priority=priority, 
            due_date=due_date if due_date else None
        )
        messages.success(request, "Task added successfully!")
        return redirect('taskboard')
    return render(request, 'add.html')

@login_required(login_url='login')
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        due_date = request.POST.get('due_date')
        task.due_date = due_date if due_date else None
        
        task.save()
        messages.success(request, "Task updated!")
        return redirect('taskboard')
    return render(request, 'edit.html', {'task': task})

@login_required(login_url='login')
def mark_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True
    task.save()
    messages.success(request, f"Task '{task.title}' marked as done!")
    return redirect('taskboard')

@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        messages.warning(request, "Task deleted successfully.")
    return redirect('taskboard')

# --- 4. AUTHENTICATION LOGIC ---

def register_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        u_email = request.POST.get('email')
        u_pass = request.POST.get('password')
        u_conf_pass = request.POST.get('confirm_password')

        if u_pass != u_conf_pass:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=u_name).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        User.objects.create_user(username=u_name, email=u_email, password=u_pass)
        messages.success(request, "Account created! Please login.")
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        u_pass = request.POST.get('password')
        user = authenticate(request, username=u_name, password=u_pass)
        if user is not None:
            login(request, user)
            return redirect('taskboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')