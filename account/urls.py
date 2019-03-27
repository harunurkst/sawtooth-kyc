from django.urls import path

from account import views

urlpatterns = [
    path('create', views.CreateAccount.as_view()),
    path('check/<account_number>', views.CheckAccount.as_view())
]