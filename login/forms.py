from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class LoginForm(forms.Form):

    email = forms.CharField(required=True,
                           error_messages={'required': 'Required Field'},
                           widget=forms.TextInput(),
    )
    passw = forms.CharField(required=True,
                           error_messages={'required': 'Required Field'},
                           widget=forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        passw = cleaned_data.get('passw')

        if email == None or passw == None:
            raise forms.ValidationError('ERROR1')
        if email == '' or passw == '':
            raise forms.ValidationError('ERROR1')

        user = authenticate(username=email, password=passw)
        if not user:
            raise forms.ValidationError('ERROR2')



class PasswordForm(forms.Form):

    email = forms.EmailField(required=True,
                           error_messages={'required': 'Required Field'},
    )

    def clean(self):
        cleaned_data = super(PasswordForm, self).clean()
        email = cleaned_data.get('email')


class RegisterForm(forms.Form):

    email = forms.EmailField(required=True,
                           error_messages={'required': 'Required Field'},
    )

    passw = forms.CharField(required=True,
                           error_messages={'required': 'Required Field'},
                           widget=forms.PasswordInput()
    )


    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        email = cleaned_data.get('email')
        passw = cleaned_data.get('passw')

        validate_password(passw)
        print(validate_password(passw))

        try:
            User.objects.create_user(email, email, passw)
        except Exception as e:
            raise forms.ValidationError(e)

        user = authenticate(username=email, password=passw)
        if not user:
            raise forms.ValidationError('Cannot Authenticate')