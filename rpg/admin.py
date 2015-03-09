from django.contrib import admin

# Register your models here.
from rpg.models import Game, Player, Item, Room

admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Item)
admin.site.register(Room)