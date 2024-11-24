from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'core/dashboard.html')

def login_view(request):
    return render(request, 'core/login.html')

def signup_view(request):
    return render(request, 'core/signup.html')

def transactions_view(request):
    return render(request, 'core/transactions.html')


