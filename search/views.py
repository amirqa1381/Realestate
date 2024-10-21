from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse
from main.models import Home
from django.db.models import Q




def search_logic(q=None, type=None,city=None,bed=None,garage=None,bath=None):
    results = Home.objects.all()
    if q:
        results = results.filter(Q(address__icontains=q) | Q(city__icontains=q) | Q(country__icontains=q))
    if type:
        results = results.filter(type=type)
    if city:
        results = results.filter(city=city)
    if bed:
        results = results.filter(beds=bed)
    if garage:
        results = results.filter(garages=garage)
    if bath:
        results = results.filter(baths=bath)
    return results



def search_func(request:HttpRequest):
    query = request.GET.get("query", None)
    type = request.GET.get("type", None)
    city = request.GET.get("city", None)
    bed = request.GET.get("bed", None)
    city = request.GET.get("city", None)
    garage = request.GET.get("garage", None)
    bath = request.GET.get("bath", None)
    results = search_logic(query, type,city,bed,garage,bath)
    context = {
        "results": results
    }
    return render(request, "search/search_result.html", context)



