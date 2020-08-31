from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}),
        error_messages={'required': 'Please enter your ID.'},
        max_length=32,
        label='ID'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class': 'form-control',}),
        error_messages={'required': 'Please enter a password.'},
        label='Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        password = cleaned_data.get('password')

        if user_id and password:
            try:
               user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                self.add_error('user_id', 'ID does not exist.')
                return

            if not check_password(password, user.password):
                self.add_error('password', 'The password is incorrect.')

def hp_validator(value):
    if len(str(value)) != 10:
        raise forms.ValidationError('Please enter the correct mobile phone number.')

def student_id_validator(value):
    if len(str(value)) != 7:
        raise forms.ValidationError('Please enter your 7 digit student number.')

class CsRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CsRegisterForm, self).__init__(*args, **kwargs)

        self.fields['user_id'].label = 'ID'
        self.fields['user_id'].widget.attrs.update({
            # 'class': 'form-control col-sm-10',
            'class': 'form-control',
            # 'placeholder': 'Please enter your ID.',
            'autofocus': False
        })
        self.fields['password1'].label = 'Password'
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': 'Please enter a password.',
        })
        self.fields['password2'].label = 'Password Confirm'
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': 'Please enter your password again.',
        })
        self.fields['email'].label = 'email'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': 'After signing up, a user verification email will be sent to the email you entered.',
        })
        self.fields['name'].label = 'Name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "It is used to find ID and password.",
        })
        self.fields['hp'].label = 'Phone Number'
        self.fields['hp'].validators = [hp_validator]
        self.fields['hp'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "Please enter a number excluding'-'",
        })
        self.fields['grade'].label = 'Grade'
        self.fields['grade'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['student_id'].label = 'Student Number'
        self.fields['student_id'].validators = [student_id_validator]
        self.fields['student_id'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "Please enter your student number.",
        })
        self.fields['circles'].label = 'Society'
        self.fields['circles'].widget.attrs.update({
            'class': 'form-control'
        })

    class Meta:
        model = User
        fields = ['user_id', 'password1', 'password2', 'email', 'name', 'hp', 'grade', 'student_id', 'circles']

    def save(self, commit=True):
        user = super(CsRegisterForm, self).save(commit=False)
        user.level = '2'
        user.department = 'Computer Sicence'
        user.is_active = False
        user.save()

        return user