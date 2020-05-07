from django.shortcuts import render


# Create your views here.

def index(request):
    my_dic = {"chance": " Hi my last kid is Puvi"}
    return render(request, 'basic_app/index.html', context=my_dic)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url.html')
