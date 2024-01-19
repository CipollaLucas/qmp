#* Acá creamos el formulario de CONTACTO

from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea)