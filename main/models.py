# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=80)
    last_picked = models.DateTimeField()

    def __unicode__(self):
        return '{}'.format(self.name)
