from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from.models import Bin

# Create your views here.
def home(request):
    # return HTTPResponse:('<h1>Hello /`.^.`\/ </h1>')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('About')
    return render(request, 'about.html')
    #context will go here as well 


def api(request):
    return JsonResponse({"status": 200})
    # this is a pulse check to make sure it works, [*super power* at the ready]




