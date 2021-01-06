from django.urls import path, include
from .views import registerPage

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', registerPage, name='register'),
]
