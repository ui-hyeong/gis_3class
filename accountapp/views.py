from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import newModel


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('input_text')  # 인풋 텍스트를 얻어 temp라는 임시데이터에 저장한다.

        model_instance = newModel()
        model_instance.text = temp
        model_instance.save()


        return HttpResponseRedirect(reverse('accountapp:hello_world'))
      # accountapp의 hello_world의 이름으로 가라

    else:
        data_list = newModel.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})