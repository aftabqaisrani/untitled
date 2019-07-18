from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from hostel.models import SignUp


def index(request):
    return HttpResponse("this is my first view !")

def detail(request, pk):
    return  HttpResponse("this is my id:" + str(pk))

def get_records(request, no_of_records):
    signups = SignUp.objects.all()
    required_records = signups[:no_of_records]
    required_records = '    '.join([str(q.pk)+' : '+q.father_name for q in required_records])
    return HttpResponse(required_records)

def get_data_by_id(request, id):
    specific_record = SignUp.objects.get(id=id)     #### get & fileter
    return HttpResponse(specific_record.father_name)
