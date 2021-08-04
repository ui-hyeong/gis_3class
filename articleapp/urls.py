from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView

app_name = 'articleapp'

#  accountapp:0000 에서 앞에accountapp같이 호출할때 app_name이 필요하다.

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),

    path('create/', ArticleCreateView.as_view(), name='create'),

    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),


]