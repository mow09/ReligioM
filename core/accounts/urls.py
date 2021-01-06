from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import registerPage

app_name = 'accounts'

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('', include('django.contrib.auth.urls')),
    # path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),

    # path('login/',
    #     auth_views.LoginView.as_view(
    #         template_name='registration/login.html'
    #     ),
    #     name='login'),

]
