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
urlpatterns = [
    
    # Acá traemos las urls de la app CORE.
     path('', include('core.urls')),

    # Acá traemos las urls de la app SERVICIOS.
     path('servicios/', include('servicios.urls')),

     # Acá traemos las urls de la app BLOG.
     path('blog/', include('blog.urls')),

    #Path del admin
    path('admin/', admin.site.urls),
]

#Si está eñ modo DEBUG activado le pasamos la dirección donde queremos que guarde los archivos media.
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
