from django.shortcuts import render


def portfolio(request):
    return render(request, 'projet_portfolio/portfolio.html')
