from django.shortcuts import render
from contact.forms import ContactForm


def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    ctx = {
        'form': form
    }
    return render(request, 'index.html', ctx)
