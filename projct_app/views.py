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
        r = requests.get(url)
        dog_json = r.json()
        context = dog_json
        # return HttpResponse(f'''<img src="{dog_json['url']}"  style="height: 500px">''')
        return render(request, 'dog.html', context=context)

class Cat(View):
    def get(self, request):
        url = 'https://aws.random.cat/meow'
        r = requests.get(url)
        cat_json = r.json()
        context = cat_json
        return render(request, 'cat.html', context=context)