from django.urls import path

from projectapp.views import ProjectCreateView, ProjectDetailView

app_name = 'projectapp'
# 이걸해야 projectapp:xxxxx 이 가능하다.


urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail')
]