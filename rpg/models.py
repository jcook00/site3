from django.db import models

# Create your models here.
from django.db import models

class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

# Create your models here.
class Game(models.Model):
    def __unicode__(self):
        return self.location
    location = models.CharField(max_length = 30)
    isover = models.BooleanField(default=False)
    stats = models.CharField(max_length = 30)

class Player(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length = 30)
    isdead = models.BooleanField(default=False)

class Item(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 50)
    quantity = models.PositiveIntegerField(default=0)

class Room(models.Model):
    def __unicode__(self):
        return self.name
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 50)
    #exits = SeparatedValuesField(max_length = 100)
    #
    def _neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def north(self):
        return self._neighbors('n')

    def south(self):
        return self._neighbors('s')

    def east(self):
        return self._neighbors('e')

    def west(self):
        return self._neighbors('w')