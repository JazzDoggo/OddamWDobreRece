from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from charity.models import Institution
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = "__all__"

