from django.shortcuts import render


# Create your views here.
def nav(request):
    
    return render(request, 'nav.html')

def index(request):
    x = {'name' : 'shyraz'}
    return render(request, 'pages\index.html', x)