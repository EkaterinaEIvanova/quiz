from registration.forms import RegistrationFormUniqueEmail
from .models import User


class RegistrationForm(RegistrationFormUniqueEmail):
    class Meta:
        model = User
        fields = ("email", 'password1', 'password2', 'name')
