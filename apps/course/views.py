from django.shortcuts import render
from contact.forms import ContactForm
from user.models import Team


def home(request):
    form = ContactForm(request.POST or None)
    team = Team.objects.all()
    if form.is_valid():
        form.save()
    ctx = {
        'form': form,
        'team': team
    }
    return render(request, 'index.html', ctx)
