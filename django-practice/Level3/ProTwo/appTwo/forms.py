from django.forms import ModelForm
from appTwo.models import User

class UserForm(ModelForm):
    class Users:
        model = User
        fields = "__all__"
