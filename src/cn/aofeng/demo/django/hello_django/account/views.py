from django.http.response import HttpResponse
from models import Student

# Create your views here.

def hello(request):
    result = Student.objects.all()
    return HttpResponse(result)