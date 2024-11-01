from django.urls import path
from .views import SignUp, login_view , logout_view

urlpatterns = [
    path('register/', SignUp.as_view(), name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
