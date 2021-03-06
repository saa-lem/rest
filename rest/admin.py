# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Property,Profile
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.
admin.site.register(Property)
admin.site.register(Profile)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')