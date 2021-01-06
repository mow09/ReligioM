from django.shortcuts import render, redirect
from django.contrib import messages
# from django.utils.translation import ugettext_lazy as _
# from django.utils.translation import gettext as _
from django.utils.translation import gettext_noop as _
from .forms import UserRegisterForm

def registerPage(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, _(f'Your account has been created, {username}! You are now able to log in.')
                )
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)
