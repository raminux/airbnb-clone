from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        # abstract models do not go into the database
        abstract = True
