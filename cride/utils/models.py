"""Django models utilities"""

# Django
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model.

    CRideModel acts as an abstract base class from which every
    other model in the project will inherent. This class provides
    every table with the following attributes:
        + create (DataTime) : Store the datatime the object was created.
        + modified (DateTime) : Store the last datatime the object was modified. 
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time in which object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time in which object was last modified'
    )

    class Meta:
        """Meta option"""

        abstract = True
        get_latest_by = 'created'
        ordering  = ['-created', '-modified']

