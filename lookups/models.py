from __future__ import unicode_literals
from datetime import datetime

from django.conf import settings
from django.db import models


class Address(models.Model):

    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'

    DIRECTIONS = (
        (None, ''),
        (NORTH, 'North'),
        (SOUTH, 'South'),
        (EAST, 'East'),
        (WEST, 'West'),
    )

    number = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=32)
    direction = models.CharField(max_length=1, choices=DIRECTIONS, null=True, blank=True)

    SUFFIX_CHOICES = (
        (None, ''),
        ('AV', 'Avenue'),
        ('BV', 'Boulevard'),
        ('CR', 'Circle'),
        ('CT', 'Court'),
        ('DR', 'Drive'),
        ('E', 'East'),
        ('EX', 'Expressway'),
        ('HY', 'Highway'),
        ('LN', 'Lane'),
        ('N', 'North'),
        ('PK', 'Park'),
        ('PL', 'Place'),
        ('RD', 'Road'),
        ('S', 'South'),
        ('ST', 'Street'),
        ('TE', 'Terrace'),
        ('TL', 'Trail'),
        ('WY', 'Way'),
        ('W', 'West'),
    )
    suffix = models.CharField(max_length=2, choices=SUFFIX_CHOICES, null=True, blank=True)

    # Last time we pulled this address from the assessors API
    last_synced = models.DateTimeField(blank=True, default=datetime.now)

    objects = AddressQuerySet.as_manager()

    def __unicode__(self):
        return "{number} {direction} {name} {suffix}".format(
            number=self.number, direction=self.get_direction_display(), name=self.name,
            suffix=self.get_suffix_display())


class Parcel(models.Model):
    number = models.PositiveSmallIntegerField(primary_key=True)
    address = models.ForeignKey('Address', related_name='parcels')

    # Last time we pulled this Parcel from the assessors API
    last_synced = models.DateTimeField(blank=True, default=datetime.now)
