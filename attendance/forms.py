from django import forms
from .models import Student

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    enter_password = forms.CharField(widget=forms.PasswordInput)
    retype_password = forms.CharField(widget=forms.PasswordInput)
    points = forms.IntegerField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Student.objects.filter(username=username).exists():
            raise forms.ValidationError('The username has been already taken.')
        return username

    def clean_enter_password(self):
        password = self.cleaned_data.get('enter_password')
        if len(password) < 5:
            raise forms.ValidationError('Password must contain 5 or more characters.')
        return password

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('enter_password')
        retyped = self.cleaned_data.get('retype_password')
        if password and retyped and (password != retyped):
            self.add_error('retype_password', 'This does not match with the above.')

    def clean_points(self):
        points = self.cleaned_data.get('points')
        if points <= 0:
            raise forms.ValidationError('Points must be greater than 0')
        return points

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('enter_password')
        points = self.cleaned_data.get('points')
        new_user = Student.objects.create_user(username=username, points=points)
        new_user.set_password(password)
        new_user.save()

class SignInForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    enter_password = forms.CharField(widget=forms.PasswordInput)
