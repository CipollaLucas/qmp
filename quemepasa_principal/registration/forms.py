from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Vamos a extender el formulario
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres máximo.") # Tiene esta longitud fija definida en el modelo UserCreationForm
    name = models.CharField(max_length=150, null=True, blank=True, default="Anónimo")
    surname = models.CharField(max_length=150, null=True, blank=True)
    specialist = models.BooleanField(default=False, null=True, blank=True, help_text="Sos especialista?")

# En este caso hacemos uso de la clase User que tiene dentro estos campos. Por eso podemos agregar "email" sin problemas.
    class Meta:
        model = User
        fields = ("first_name", "last_name","is_specialist", "username", "email", "password1", "password2") 

# Validamos el campo email
    def clean_email(self):
        #Recuperamos el email
        email = self.cleaned_data.get("email")
        #Preguntamos a la base de datos si existe, con el meto exists()
        if User.objects.filter(email=email).exists():
            #Si existe el mail, enviamos un raise con el texto.
            raise forms.ValidationError("El email ya está registrado, proba con otro.")
        return email
    

#Mejoramos el perfil
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows':3, 'placeholder': 'Biografia'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Enlace'}),
        }

#Acá creamos la clase del mail para poder modificarlo
class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres máximo.") # Tiene esta longitud fija definida en el modelo UserCreationForm

    class Meta:
        model = User
        fields = ['email']
# Validamos el campo email
    def clean_email(self):
        #Recuperamos el email
        email = self.cleaned_data.get("email")
        # Preguntamos si no existe dentro de changed_data que es quién almacena todos los datos que se estan modificando en el formulario
        if 'email' in self.changed_data:
            print(self.changed_data)
            #Preguntamos a la base de datos si existe, con el meto exists(). Porque sólo vamos a dejar guardar un mail, si no lo tiene otro usuario antes.
            if User.objects.filter(email=email).exists():
                #Si existe el mail, enviamos un raise con el texto.
                raise forms.ValidationError("El email ya está registrado, proba con otro.")
            return email
        