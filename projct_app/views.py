from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import requests

# Create your views here.
class Hom(View):
    def get(self, request):
        context = {}
        return render(request, 'hom.html', context = context)


class Dog(View):
    def get(self, request):
        url = 'https://random.dog/woof.json'
        request = requests.get(url)
        dog_json = request.json()
        context = dog_json
        return render(request, 'dog.html', context = context)

class Cat(View):
    def get(self, request):
        url = 'https://aws.random.cat/meow'
        request = requests.get(url)
        cat_json = request.json()
        context = cat_json
        return render(request, 'cat.html', context = context)
