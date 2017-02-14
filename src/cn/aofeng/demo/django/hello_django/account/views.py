#coding=utf-8

from django.http.response import HttpResponse
from models import Student
import logging

# Create your views here.

def hello(request):
    logging.getLogger("stats").info("method:%s, remote addr:%s", request.META['REQUEST_METHOD'], request.META['REMOTE_ADDR'])
    result = Student.objects.all()
    return HttpResponse(result)