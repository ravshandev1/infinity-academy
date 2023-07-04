from django.urls import path, include

urlpatterns = [
    path('', include('course.urls')),
    path('user/', include('user.urls')),
    path('contact/', include('contact.urls')),
]
