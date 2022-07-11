# forms.py in the 'auth1app' directory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Give us your email address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your first name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your last name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        helper_text = '''
        <ul>
        <li>Your password can’t be too similar to your other personal information.</li>
        <li>Your password must contain at least 8 characters.</li>
        <li>Your password can’t be a commonly used password.</li>
        <li>Your password can’t be entirely numeric.</li>
        </ul>

        '''

        # Again, all this nonsense is because we didn't just build a form like the login screen
        # This is customizing the built-in django stuff: obnoxious
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Make up a cool username.'
        self.fields['username'].help_text = '<small class="form-text text-muted"><i>Username must contain letters, digits, and " @ . + - _ " only.</i></small>'
        self.fields['username'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Generate a password'
        self.fields['password1'].help_text = '<small class="form-text text-muted"><i>{}</i></small>'.format(helper_text)
        self.fields['password1'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm the password'
        self.fields['password2'].help_text = ''
        self.fields['password2'].label = ''



class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Updateyour email address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Update first name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Update last name'}))
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        # Again, all this nonsense is because we didn't just build a form like the login screen
        # This is customizing the built-in django stuff: obnoxious
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Change your username.'
        self.fields['username'].help_text = '<small class="form-text text-muted"><i>Username must contain letters, digits, and " @ . + - _ " only.</i></small>'
        self.fields['username'].label = ''

