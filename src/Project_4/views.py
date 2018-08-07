from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
import random

def home(request):
    return render(request, 'home.html', {})

# just trying out function and class based views
# to see how it all works and which I prefer

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'name': 'Darren',
            'random': random.randint(500, 1000)
        }
        return render(request, 'home.html', context)

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('Hello')
    #
    # def put(self, request, *args, **kwargs):
    #     return HttpResponse('Hello')
    #
    # def delete(self, request, *args, **kwargs):
    #     return HttpResponse('Hello')
