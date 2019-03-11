from django.urls import path

from account.views import CreateAccount

urlpatterns = [
    path('create', CreateAccount.as_view())
]