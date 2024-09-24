from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse


def serach_func(request:HttpRequest):
    qu = request.POST.get("query", None)
    bed = request.POST.get("bed", None)
    print(qu)
    print(bed)
    return redirect(reverse("index"))   