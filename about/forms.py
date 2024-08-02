from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    Form class for users to request a collaboration
    """

    class Meta:
        model = CollaborateRequest
        fields = ("name", "email", "message")
