from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import newModel


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('input_text')  # 인풋 텍스트를 얻어 temp라는 임시데이터에 저장한다.

        model_instance = newModel()
        model_instance.text = temp
        model_instance.save()

        data_list = newModel.objects.all()


        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})

    else:
        data_list = newModel.objects.all()


        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})