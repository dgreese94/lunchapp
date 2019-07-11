# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytz
from datetime import datetime, timedelta
from numpy.random import choice
from django.shortcuts import render
from main import models


def weight_persons(persons):
    weighted_person_dict = {}
    days_since_per_person = {}
    now = datetime.utcnow().replace(tzinfo=pytz.utc)
    for person in persons:
        days_since_per_person[person] = (now - person.last_picked).total_seconds()
    total_seconds = sum(days_since_per_person.values())
    for k, v in days_since_per_person.iteritems():
        weighted_person_dict[k] = v/total_seconds
    return weighted_person_dict


def index(request):
    persons = models.Person.objects.all()
    weighted_group = weight_persons(persons)
    data = {'data': weighted_group}
    return render(request, "index.html", data)

def results(request):
    data = {}
    persons = models.Person.objects.all()
    weighted_group = weight_persons(persons)
    picker = choice(weighted_group.keys(), 1, p=weighted_group.values())[0]
    data['picker'] = picker
    picker.last_picked = datetime.now()
    picker.save()
    return render(request, "results.html", data)
