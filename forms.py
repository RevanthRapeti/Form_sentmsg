from django import forms
from .models import Snippet

GEEKS_CHOICES =(
    ("cold/cough/fever", "Cold/Cough/Fever"),
    ("migraine", "Migraine"),
    ("sugar-test", "sugar-test"),
    ("body-checkup", "Body-checkup"),
    ("Others", "Other"),
)


class InputForm(forms.Form):
    Name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    Issue = forms.ChoiceField(choices=GEEKS_CHOICES)
    Description = forms.CharField(required=False)
    covid_affected = forms.BooleanField()
    phone_no = forms.IntegerField()


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = '__all__'
