from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import RegisterForm

from django.contrib.auth import logout


class RegisterView(View):
    template_name = "app_auth/register.html"
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Hello {username}. Registration complete')
            return redirect(to='app_auth:signin')
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        # return redirect('app_auth:signin')