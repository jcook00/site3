from django.db import models
import yaml


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return yaml.load(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return yaml.dump(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


class Game(models.Model):
    def __unicode__(self):
        return self.location
    location = models.CharField(max_length=30)
    introduction = models.TextField(default="in the room")
    cmd = models.CharField(max_length=30, default=None)


class Room(models.Model):
    def __unicode__(self):
        return "Item(%s)" % self.name
    name = models.CharField(max_length=30)
    description = models.TextField()
    neighbors = ListField(null=True)
    exits = ListField(null=True)
    items = ListField(null=True)


class Player(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=30, default='player1')
    session = models.TextField(null=True)
    inventory = ListField(default=None)
    location = models.CharField(max_length=30)
    isdead = models.BooleanField(default=False)


class Item(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    items = ListField(default=None)

    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None