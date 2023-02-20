from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="ФИО", required=True)
    age = forms.IntegerField(label="Возраст", required=True)
