from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message, User

admin.site.register(User)
admin.site.register(Room)  # this basically registers the room into the admin panel
admin.site.register(Topic)
admin.site.register(Message)
