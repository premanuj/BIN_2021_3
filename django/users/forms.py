from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        # exclude = ('adress', 'role')
    
    def clean_email(self):
        try:
            email = self.cleaned_data['email']
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        else:
            raise ValidationError("Email already exists.")
        
