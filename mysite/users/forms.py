from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control',}),
        error_messages={'required': '아이디을 입력해주세요.'},
        max_length=32,
        label='ID'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
        attrs={'class': 'form-control',}),
        error_messages={'required': '비밀번호를 입력해주세요.'},
        label='비밀번호'
    )

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        password = cleaned_data.get('password')

        if user_id and password:
            try:
               user = User.objects.get(user_id=user_id)
            except User.DoesNotExist:
                self.add_error('user_id', '아이디가 존재하지 않습니다.')
                return

            if not check_password(password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')

def hp_validator(value):
    if len(str(value)) != 10:
        raise forms.ValidationError('정확한 핸드폰 번호를 입력해주세요.')

def student_id_validator(value):
    if len(str(value)) != 7:
        raise forms.ValidationError('본인의 학번 7자리를 입력해주세요.')

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