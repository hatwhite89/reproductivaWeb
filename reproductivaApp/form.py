from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class correo(forms.Form):

    asunto=forms.CharField(required=True)
    correo=forms.EmailField()
    contenido=forms.CharField( widget=forms.Textarea)
