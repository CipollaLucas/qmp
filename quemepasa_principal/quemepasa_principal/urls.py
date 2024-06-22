"""
URL configuration for quemepasa_principal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.conf import settings
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns


urlpatterns = [
    
    # Acá traemos las urls de la app CORE.
    path('', include('core.urls')),

    # Acá traemos las urls de la app SERVICIOS.
    path('servicios/', include('servicios.urls')),

    # Acá traemos las urls de la app BLOG.
    path('blog/', include('blog.urls')),

    # Acá traemos las urls de la app PAGES.
    path('page/', include('pages.urls')),

    # Acá traemos las urls de la app CONTACTO.
    path('contacto/', include('contacto.urls')),

    #Path del admin
    path('admin/', admin.site.urls),
    
    # Path de Auth - Incluímos esto, debido a Django nos proveerá urls para el manejo de la autenticación.
    # Automaticamente se nos crearán urls para el manejo todal de las cuentas. Docu --> https://ccbv.co.uk/
    path('accounts/', include ('django.contrib.auth.urls')),
    path('accounts/', include ('registration.urls')),

    #Path de Profiles
    path('profiles/', include (profiles_patterns)),

    #Path de messenger
    path('messenger/', include(messenger_patterns))
]

#Si está eñ modo DEBUG activado le pasamos la dirección donde queremos que guarde los archivos media.
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
