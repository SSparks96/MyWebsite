from django import forms


class FirstNameForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
