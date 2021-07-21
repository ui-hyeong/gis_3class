from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import newModel


def hello_world(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('input_text')  # 인풋 텍스트를 얻어 temp라는 임시데이터에 저장한다.

            model_instance: newModel = newModel()
            model_instance.text = temp
            model_instance.save()


            return HttpResponseRedirect(reverse('accountapp:hello_world'))
          # accountapp의 hello_world의 이름으로 가라

        else:
            data_list = newModel.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})

    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html' #어떤 html페이지를 쓸지

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm                            # 아이디도 바꿀수 있게 설정되어있어서 forms를 직접만들어 대신 넣어줌
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):             # 주소를 직접 입력해서 접근해도 로그인 화면으로 넘어가게 한다.
        if request.user.is_authenticated and self.get_object() == request.user:  # 로그인 확인 여부  //  self.get_object() == target_user와 동일이다.
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()   # 접근금지 응답 송출

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):             # 주소를 직접 입력해서 접근해도 로그인 화면으로 넘어가게 한다.
        if request.user.is_authenticated and self.get_object() == request.user:  # 로그인 확인 여부  //  self.get_object() == target_user와 동일이다.
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()   # 접근금지 응답 송출

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()