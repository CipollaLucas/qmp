from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from .forms import UserCreationFormWithEmail, ProfileForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile


# Vamos a crear el formulario de registro heredando de las clases que ya trae Django.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    #Este metodo nos permitira modiicar en tiempo real el redireccionamiento.
    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    
    #Este metodo recupera el formulario login.
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Modificamos un widget en tiempo real, esto lo hacemos acá para poder mantener las validaciones que trae por defecto el form de django.
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Elija un nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder': 'DIreccion de email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Elija una contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Repita la contraseña'})
        return form


@method_decorator(login_required, name='dispatch') 
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    #fields = ['avatar', 'bio', 'link'] Lo comento porque ya vienen definidos en el form.
    success_url = reverse_lazy('profile')
    template_name= 'registration/profile_form.html'

    #Vamos a recuperar el usuario
    def get_object(self):
        # recuperamos el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user) # si no lo encuentra lo crea. devuelve una tupla: el prifle, y una variable booleano.
        return profile
