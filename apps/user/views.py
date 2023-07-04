from django.shortcuts import render
from .models import Subscribe
from django.http import JsonResponse


def subscribe(request):
    email = request.GET.get('email')
    print(email)
    # Subscribe.objects.create(email=email)
    return JsonResponse({'message': "Thank you"})

