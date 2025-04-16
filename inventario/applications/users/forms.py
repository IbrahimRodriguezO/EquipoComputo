from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña"
            }
        )
    )

    password2 = forms.CharField(
        label="Repetir contraseña",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repetir contraseña"
            }
        )
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "nombres",
            "apellidos",
            "role",
            "is_staff",
            "is_active",
        )
        
    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if len(password1) < 8:
            self.add_error("password1", "La contraseña es menor a 8 carácteres")

        if password1 != password2:
            self.add_error("password2", "Las contraseñas no son las mismas")


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter a valid email address",
                "id": "username",
            }
        )
    )
    password = forms.CharField(
        label="Contraseña",
        required=True,
        widget=forms.TextInput(  # ← CAMBIO: Antes era PasswordInput
            attrs={
                "class": "form-control form-control-lg",  # ← Agregamos 'form-control'
                "placeholder": "Contraseña",
                "id": "password",
                "type": "password"  # ← Definimos el tipo manualmente
            }
        )
    )


    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]

        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Los datos del usuario no son correctos")

        return super(LoginForm, self).clean()
    

class UpdateUser(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "nombres",
            "apellidos",
            "role",
            "is_staff",
            "is_active",
        )
