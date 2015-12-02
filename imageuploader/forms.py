from django import forms


class IMGForm(forms.Form):
    # image upload form
    imgField = forms.ImageField(label='Choose File')
