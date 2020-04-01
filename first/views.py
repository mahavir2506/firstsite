from django.shortcuts import render
from  first.models import User

# Create your views here.

def index(request):
	return render(request,'index.html')

def users(request):

	user_list=User.objects.order_by('first_name')
	return render(request,'users.html',{"user":user_list})