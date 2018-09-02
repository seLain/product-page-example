from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def support(request):
	return render(request, 'support.html', {})