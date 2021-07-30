from django.urls import path
from django.views.generic import TemplateView

app_name = 'articleapp'

#  accountapp:0000 에서 앞에accountapp같이 호출할때 app_name이 필요하다.

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list')
]