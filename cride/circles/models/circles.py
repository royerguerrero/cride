"""Circle model"""

# Django
from django.db import models

# Utilitis 
from cride.utils.models import CRideModel

class Circle(models.Model):
    """Circle model.
    
    A circle is a privete group where rides are offerted and taken
    by its member, To join a circle a user must recieve an unique
    invitacion code from an exixting circle member   
    """

    name = models.CharField('cicle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('Cicle description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True)

    # Stats
    rides_offerted = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles are alse know as official communities.'   
    )

    is_public = models.BooleanField(
        default='True',
        help_text='Public circles are listed the main page so everyone know about their existence.'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members'
    )

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If circle is limited this will be the limit on the number of menbers.'
    )

    def __str__(self):
        """Return name of circle"""
        return str(self.name)

    class Meta(CRideModel.Meta):
        """Meta class."""

        ordering = ['-rides_taken', '-rides_offerted']