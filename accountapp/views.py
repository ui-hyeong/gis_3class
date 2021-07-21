from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import newModel

@login_required # login_url을 선언하여 경로를 설정해 줄 수 있다.
def hello_world(request):

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



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html' #어떤 html페이지를 쓸지

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(login_required, 'get')  #함수에 쓰일 데코레이터를 메서드에도 적용시킨다. login을 어디에 적용시킬지도 작성해야한다.
@method_decorator(login_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm                            # 아이디도 바꿀수 있게 설정되어있어서 forms를 직접만들어 대신 넣어줌
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'




@method_decorator(login_required, 'get')  #함수에 쓰일 데코레이터를 메서드에도 적용시킨다. login을 어디에 적용시킬지도 작성해야한다.
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

