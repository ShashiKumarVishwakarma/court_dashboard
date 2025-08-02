from django import forms

class CaseForm(forms.Form):
    case_type = forms.CharField(label='Case Type', max_length=20)
    case_number = forms.CharField(label='Case Number', max_length=10)
    case_year = forms.CharField(label='Filing Year', max_length=4)

