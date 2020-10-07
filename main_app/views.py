from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Bin, Person, Investor, Collection_Market
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



# BINS INDEX
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

# BINS SHOW DETAIL
def bins_detail(request, bin_id):
    bin = Bin.objects.get(id=bin_id)
    context = {'bin': bin}
    return render(request, 'bins/detail.html',context)

# BINS EDIT && UPDATE
def bins_edit(request, bin_id):
  bin = Bin.objects.get(id=bin_id)
  if request.method == 'POST':
    bin_form = Bin_Form(request.POST, instance=bin)
    if bin_form.is_valid():
      bin_form.save()
      return redirect('detail', bin_id=bin_id)
  else:  
    # in form(instance=The object that we pull back from db)
    bin_form = Bin_Form(instance=bin)
  context = {'bin': bin, 'bin_form': bin_form}
  return render(request, 'bins/edit.html', context)


# BINS DELETE
def bins_delete(request, bin_id):
    Bin.objects.get(id=bin_id).delete()
    return redirect("bins_index")





# BUSINESS INDEX
def businesses_index(request):
    if request.method =='POST':
        business_form = Business_Form(request.POST)
        if business_form.is_valid():
            business_form.save()
            return redirect('businesses_index')
    businesses = business.objects.all()
    business_form = Business_Form()
    context = {'businesses' : businesses, 'business_form':Business_form}
    return render(request, 'businesses/index.html',context)


# BUSINESS SHOW DETAIL
def businesses_detail(request, business_id):
    business = business.objects.get(id=business_id)
    context = {'business': business}
    return render(request, 'businesses/detail.html',context)

# BUSINESS EDIT && UPDATE
def businesses_edit(request, business_id):
  business = Business.objects.get(id=business_id)
  if request.method == 'POST':
    business_form = Business_Form(request.POST, instance=business)
    if business_form.is_valid():
      business_form.save()
      return redirect('detail', business_id=business_id)
  else:  
    # in form(instance=The object that we pull back from db)
    business_form = Business_Form(instance=business)
  context = {'business': business, 'business_form': business_form}
  return render(request, 'businesses/edit.html', context)


# BUSINESS DELETE
def businesses_delete(request, business_id):
    Business.objects.get(id=business_id).delete()
    return redirect("businesses_index")





# PERSON INDEX
def persons_index(request):
    if request.method =='POST':
        person_form = Person_Form(request.POST)
        if person_form.is_valid():
            person_form.save()
            return redirect('persons_index')
    persons = person.objects.all()
    person_form = Person_Form()
    context = {'persons' : persons, 'person_form':Person_form}
    return render(request, 'persons/index.html',context)

# PERSON SHOW DETAIL
def persons_detail(request, person_id):
    person = Person.objects.get(id=person_id)
    context = {'person': person}
    return render(request, 'persons/detail.html',context)

# PERSON EDIT && UPDATE
def persons_edit(request, person_id):
  person = Person.objects.get(id=person_id)
  if request.method == 'POST':
    person_form = Person_Form(request.POST, instance=person)
    if person_form.is_valid():
      person_form.save()
      return redirect('detail', person_id=person_id)
  else:  
    # in form(instance=The object that we pull back from db)
    person_form = Person_Form(instance=person)
  context = {'person': person, 'person_form': person_form}
  return render(request, 'persons/edit.html', context)

# PERSON DELETE
def persons_delete(request, person_id):
    Person.objects.get(id=person_id).delete()
    return redirect("persons_index")





# COLLECTION_MARKET INDEX
def collection_markets_index(request):
    if request.method =='POST':
        collection_market_form = Collection_Market_Form(request.POST)
        if collection_market_form.is_valid():
            collection_market_form.save()
            return redirect('collection_markets_index')
    collection_markets = collection_market.objects.all()
    collection_market_form = Collection_Market_Form()
    context = {'collection_markets' : collection_markets, 'collection_market_form':Collection_Market_Form}
    return render(request, 'collection_markets/index.html',context)

# COLLECTION_MARKET SHOW DETAIL
def collection_markets_detail(request, bin_id):
    collection_market = Collection_Market.objects.get(id=collection_market_id)
    context = {'collection_market': collection_market}
    return render(request, 'collection_markets/detail.html',context)

# COLLECTION_MARKET EDIT && UPDATE
def collection_markets_edit(request, bin_id):
  collection_market = Collection_Market.objects.get(id=collection_market_id)
  if request.method == 'POST':
    collection_market_form = Collection_Market_Form(request.POST, instance=collection_market)
    if collection_market_form.is_valid():
      collection_market_form.save()
      return redirect('detail', collection_market_id=collection_market_id)
  else:  
    # in form(instance=The object that we pull back from db)
    collection_market_form = Collection_Market_Form(instance=collection_market)
  context = {'collection_market': collection_market, 'collection_market_form': collection_market_form}
  return render(request, 'collection_markets/edit.html', context)


# COLLECTION_MARKET DELETE
def collection_markets_delete(request, collection_market_id):
    Collection_Market.objects.get(id=collection_market_id).delete()
    return redirect("collection_markets_index")


