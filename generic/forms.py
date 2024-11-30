from django import forms


class AddContentForm(forms.Form):
    file = forms.FileField(required=True,)
    description = forms.CharField(widget=forms.Textarea, required=True)
