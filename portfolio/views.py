from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/home.html')


def legal_notice(request):
    return render(request, 'portfolio/legal_notice.html')

def log_in(request):
    return render(request, 'portfolio/log_in.html')
