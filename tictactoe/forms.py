from django.forms import ModelForm
from .models import Invitation

class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        fields = '__all__'