from django.shortcuts import render

def index(request):
    context = locals()
    template = 'index.html'
    return render(request, 'main/index.html')

def about(request):
    context = locals()
    template = 'about.html'
    return render(request, 'main/about.html')
