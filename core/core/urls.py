from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    # admin comes last - no overwrite of logout
    path('admin/', admin.site.urls),
]
