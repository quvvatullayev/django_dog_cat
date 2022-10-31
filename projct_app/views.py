from django.http import HttpResponse, JsonResponse
from django.views import View
import requests

# Create your views here.
class Hom(View):
    def get(self, request):
        return HttpResponse('salom')

class Dog(View):
    def get(self, request):
        url = 'https://random.dog/woof.json'
        request = requests.get(url)
        dog_json = request.json()
        return JsonResponse(dog_json)

class Cat(View):
    def get(self, request):
        url = 'https://aws.random.cat/meow'
        request = requests.get(url)
        cat_json = request.json()
        return JsonResponse(cat_json)