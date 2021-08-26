from django import forms
from django.shortcuts import render
from django.views.generic import View
from users.forms import UserRegistrationForm

# Create your views here.
class UserResigtrationView(View):
    template_name = "users/registration.html"
    def get(self, request, *args, **kwargs):
        form = {'form': UserRegistrationForm()}
        return render(request, self.template_name, form)

    def post(self, request, *args, **kwargs):
        
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            template_name = "users/success.html"
            return render(request, template_name, {'user': user})
        else:
            return render(request, self.template_name, {'form':form})
        # return render(request, template_name, form)