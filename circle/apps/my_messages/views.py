from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hello(request):
    if request.method == "GET":
        return JsonResponse({"message":"Hello World!"}, status=200)

def goodbye(request):
    if request.method == "GET":
        return JsonResponse({"message":"See ya bro!"}, status=200)

def ciao(request):
    if request.method == "GET":
        return JsonResponse({"message":"Ciao!"}, status=200)
