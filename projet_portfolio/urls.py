from django.urls import path

from . import views

app_name = "projet_portfolio"

urlpatterns = [
    path('portfolio/', views.portfolio, name="portfolio"),
]
