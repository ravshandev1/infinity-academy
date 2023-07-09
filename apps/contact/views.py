from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from user.models import Team


def contact(request):
    form = ContactForm(request.POST or None)
    qs = Contact.objects.all()
    print(qs)
    ctx = {
        'form': form
    }
    return render(request, 'contact.html', ctx)


def about(request):
    team = Team.objects.all()
    ctx = {
        'team': team
    }
    return render(request, 'about-us.html', ctx)
