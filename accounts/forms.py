from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='ID',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    last_name = forms.CharField(
        label='성',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    first_name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    birthday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            },
        ),
    )

    profile_image = forms.ImageField(
        label='프로필 이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control form-control-sm',
            },
        ),
        required=False,
    )

    email = forms.CharField(
        label='e-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
            },
        ),
    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
            },
        ),
    )

    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
            },
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'last_name',
            'first_name',
            'birthday',
            'profile_image',
            'email',
            'password1',
            'password2',
        )


class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(
        label='ID',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    birthday = forms.DateField(
        label='생년월일',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
            },
        ),
    )

    profile_image = forms.ImageField(
        label='프로필 이미지',
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control form-control-sm',
            },
        ),
    )

    email = forms.CharField(
        label='e-mail',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
            },
        ),
    )

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'birthday',
            'profile_image',
            'email',
        )


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='ID',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            },
        ),
    )

    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'type': 'password',
            },
        ),
    )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )