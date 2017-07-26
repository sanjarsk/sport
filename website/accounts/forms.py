from registration.forms import RegistrationForm
from .models import User

class CustomUserForm(RegistrationForm):
    class Meta:
        model = User
        exclude = ['is_active', 'is_staff',]