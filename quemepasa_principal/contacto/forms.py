#* Acá creamos el formulario de CONTACTO

from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea)

"""class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactoModelo
        fields = ['Nombre', 'Email', 'Contenido']
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'contenido' : forms.Textarea(attrs={'class':'form-control'})
        }
        labels = {
            'nombre' : '', 'email':'', 'contenido': ''
        }"""