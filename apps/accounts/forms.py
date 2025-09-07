from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomSignupForm(SignupForm):
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea(attrs={'rows': 4}))
    location = forms.CharField(max_length=30, required=False)
    birth_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.bio = self.cleaned_data['bio']
        user.location = self.cleaned_data['location']
        user.birth_date = self.cleaned_data['birth_date']
        user.save()
        return user


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "bio", "location", "birth_date")
