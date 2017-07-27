from registration.forms import RegistrationForm
from .models import User

class CustomUserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'faculty', 'phone_number',]