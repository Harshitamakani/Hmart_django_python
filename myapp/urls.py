from django.urls import path
from myapp import views

# from allauth.account.views import (LoginView)

urlpatterns = [
    path('',views.index,name='home')
    # path('', LoginView.as_view(template_name='account/login.html'), name='account_login'),
]
