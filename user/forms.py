from django.forms import ModelForm
from user.models import User
from django.utils.translation import gettext_lazy as _


class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ["name", "email", "username", "is_teacher", "is_student"]
        labels = {
            "name": _("Name"),
        }
        error_messages = {
            "name": {
                "max_length": _("O nome está muito longo"),
            },
        }
