from django.forms import ModelForm
from user.models import User
from django.utils.translation import gettext_lazy as _


class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = ["name", "email", "username"]
        labels = {
            "name": _("Name"),
        }
        help_texts = {
            "name": _("Example: João Silva"),
        }
        error_messages = {
            "name": {
                "max_length": _("O nome está muito longo"),
            },
        }
