from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(templates_name='accountapp/login.html'), name='login'),  # loginview는 장고에서 제공해주는 클래스

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create') # as_view를 선언하여 클래스를 사용할 수있게 한다.


]

