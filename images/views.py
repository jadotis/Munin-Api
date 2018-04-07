from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    print(request.get_full_path())
    image_name = request.get_full_path().replace('images/', '').replace('/','')
    pathname = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\Api\\Static\\' + image_name + '.jpg'
    print(pathname)
    image_data = open(pathname, "rb").read()
    return HttpResponse(image_data, content_type="image/jpg")
    #Dynamically builds out the path

