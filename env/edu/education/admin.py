# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(course)

admin.site.register(semester)

admin.site.register(student)
admin.site.register(feedback)


admin.site.register(subject)
admin.site.register(marks)

admin.site.register(attendance)
admin.site.register(fee)
admin.site.register(material)

admin.site.register(department)
