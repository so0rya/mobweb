from django import forms

class MobileCreateForm(forms.Form):
    mobile_id = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    mobile_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    brand= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    price= forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    network= forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))