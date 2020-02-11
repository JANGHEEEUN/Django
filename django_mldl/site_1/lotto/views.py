from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #site_1\lotto\templates\lotto\default.html
    return render(request, 'lotto/default.html', {})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")
