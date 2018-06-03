from django.shortcuts import render,redirect
from django.http import HttpResponse
from authorization.models import Authorization
from django.views.generic import ListView,DetailView
from authorization.forms import Auth_Create
# Create your views here.
def home(request):
	return render(request,'authorization/home.html')

def createauth(request):
	if request.method=='POST':
		form=Auth_Create(request.POST)
		form.save()
		return redirect('all_auths')
	else:
		form=Auth_Create()
	return render(request,'authorization/createauth.html',{'form':form})

class Auth_ListView(ListView):
	model=Authorization


class Auth_DetailView(DetailView):
	model=Authorization
