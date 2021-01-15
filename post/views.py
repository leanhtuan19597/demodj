
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post(request):
	return HttpResponse('Đây là page 1')
def postnew(request):
	return HttpResponse('Đây là page new')