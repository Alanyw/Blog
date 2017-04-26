from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello,world.You're at the article index")


def title(request, title_id):
    response = "You're looking at the results of article %s "
    print(title_id)
    return HttpResponse(response % title_id)
