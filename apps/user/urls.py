from django.urls import path
from .views.login import LoginView
from .views.register import RegisterView
from .views.logout import LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
