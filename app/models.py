# models.py

from banjo.models import Model, StringField, IntegerField, FloatField, BooleanField

class Quotes(Model):
    quote = StringField()
    hint = StringField()
    likes = IntegerField()
    difficulty = IntegerField()
    correct_percentage = FloatField()


