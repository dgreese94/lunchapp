# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main import models as mModels

admin.site.register(mModels.Person)
