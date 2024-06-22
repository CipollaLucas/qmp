from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Creamos las clases de la app Messenger.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Importamos al usuario. No debemos dejar que el usuario borre instancias.
    content = models.TextField()                             # Contenido del mensaje
    created = models.DateTimeField(auto_now=True)            # Fecha y hora.

    class Meta:
        ordering = ['created']

#Creamos esto para poder definir nuestros métodos de consulta
class ThreadManager(models.Manager):
    def find(self, user1, user2):
        queryset = self.filter(users=user1).filter(users=user2) # Contiene todas las instnacias. O lo mismo que Thread.objects.all()
        if len(queryset) > 0:
            return queryset[0]
        return None
    
    def find_or_create(self, user1, user2):
        #buscamos si el hilo existe
        thread = self.find(user1, user2)
        if thread is None:
            #Creamos el hilo
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread
    
#Esta compuesto por campos manytomany
class Thread(models.Model):
    
    users = models.ManyToManyField(User, related_name='threads')    # Aca mediante un 'user.threads' podremos acceder a todas los hilos a los que el usuario pertenece.
    messages = models.ManyToManyField(Message)                      # Se almacenan todos los mensajes que forman parte del hilo.

    objects = ThreadManager()



# Señal
def messages_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None)             # Intancia que manda la señal.
    action= kwargs.pop("action", None)                  # Accion que se está ejecutando. Aca se busca el pre add, el momento antes del mensaje.
    pk_set= kwargs.pop("pk_set", None)                  # Conjunto donde se van a recuperar los mensajes.
    print(instance, action, pk_set)

    # Comprobamos que los que componen el hilo existan y formen parte de el.

    false_pk_set = set()# declaramos un conjunto para guardar los mensajes fraudulentos
    
    if action is "pre_add":                 # Primero que sea pre_add
        for msg_pk in pk_set:               # Buscamos en los mensajes los pk.
            msg = Message.objects.get(pk=msg_pk)                    # Acá los recuperamos
            if msg.user not in instance.users.all():                # Comprobamos que el autor exista dentro de la instancia del hilo.
                print("Ups, ({}) no forma parte del hilo.".format(msg.user))
                false_pk_set.add(msg_pk)

    # Buscamos los mensajes del conjunto flase_pk_set para luego eliminarlos
    pk_set.difference_update(false_pk_set)  # Esto hace es cómo si le restara al pk_set inicial, los false_pk_set y "limpiar el hilo".

#Conectamos la señal
m2m_changed.connect(messages_changed, sender=Thread.messages.through) # con esto queda atento a cualquier cambio que ocurra en el campo manytomany messages