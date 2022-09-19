from django import forms


class HashForm(forms.Form):
    text = forms.CharField(required=False)
    alg_name = forms.CharField(required=True)
