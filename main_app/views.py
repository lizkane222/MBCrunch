from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Bin, Investor
from .forms import Bin_Form, Investor_Form
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


def bins_index(request):
    if request.method =='POST':
        bin_form = Bin_Form(request.POST)
        if bin_form.is_valid():
            bin_form.save()
            return redirect('bins_index')
    bins = Bin.objects.all()
    bin_form = Bin_Form()
    context = {'bins' : bins, 'bin_form':bin_form}
    return render(request, 'bins/index.html',context)





def bins_detail(request, bin_id):
    bin = Bin.objects.get(id=bin_id)
    context = {'bin': bin}
    return render(request, 'bins/detail.html',context)