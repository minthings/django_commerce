from django.shortcuts import render
from contact.forms import contactForm

def contact(request):
    form = contactForm(request.POST)
    if form.is_valid():
        return request.POST
    context = locals()
    template = 'contact.html'
    return render(request, 'contact/contact.html', context)
