from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def insert_topic(request):
    topic=input('Enter Topic Name:')
    TO=Topic.objects.get_or_create(topic_name=topic)[0]
    TO.save()
    return HttpResponse('<center><h1>Topic Data is Inserted</h1></center>')

def insert_webpage(request):
    topic=input('Enter Topic Name:')
    TO=Topic.objects.get_or_create(topic_name=topic)[0]
    TO.save()
    na=input('Enter Name:')
    ur=input('Enter URL:')
    WO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()
    return HttpResponse('<center><h1>Webpage Data is Inserted</h1></center>')

def insert_accessrecord(request):
    topic=input('Enter Topic Name:')
    TO=Topic.objects.get_or_create(topic_name=topic)[0]
    TO.save()
    na=input('Enter Name:')
    ur=input('Enter URL:')
    WO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
    WO.save()
    da=input('Enter Date:')
    au=input('Enter Author Name:')
    AO=AccessRecord.objects.get_or_create(name=WO,date=da,author=au)
    AO.save()
    return HttpResponse('<center><h1>AccessRecord Data is Inserted</h1></center>')