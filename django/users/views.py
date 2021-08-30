from django import forms
from django.contrib.auth import tokens
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from users.forms import UserRegistrationForm
from users.models import Role, User
from django.http import Http404
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from users.tokens import activation

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
            try:
                role = get_object_or_404(Role, pk=1)
                print("Role found")
            except Http404:
                print("Role not found.")
                role = Role.objects.create(pk=1)
            user.save()
            user.role.add(role)
            user_email = form.cleaned_data['email']
            email_html = "users/registration_email.html"
            email_template = render_to_string(
                email_html,
                {
                    "domain": request.get_host(),
                    "uid": urlsafe_base64_encode(force_bytes(user.id)),
                    "token": activation.make_token(user)
                }
            )
            email_subject = "Activate your account"
            send_email = EmailMessage(email_subject, email_template, to=[user_email])
            send_email.content_subtype = "html"
            send_email.send()
            template_name = "users/success.html"
            return render(request, template_name, {'user': user})
        else:
            return render(request, self.template_name, {'form':form})
        # return render(request, template_name, form)

def activate_user(request, ub64, token):
    user_id = force_text(urlsafe_base64_decode(ub64))
    try:
        user = get_object_or_404(User, pk=user_id)
    except Http404:
        return render(request, 'users/invalid_token.html', {'error': "User not exist"})
    else:
        try:
            print(token)
            activation.check_token(user, token)
        except Exception:
            return render(request, 'users/invalid_token.html', {'error': "Invalid Token"})
        user.is_active = True
        user.save()
        return render(request, 'users/activation_success.html', {'user': user})