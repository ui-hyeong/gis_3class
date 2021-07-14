from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/', AccountCreateView.as_view(), name='create') # as_view를 선언하여 클래스를 사용할 수있게 한다.


]

