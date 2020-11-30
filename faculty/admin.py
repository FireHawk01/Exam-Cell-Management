from django.contrib import admin

from .models import Announcements, Syllabus, Calendar, Questionp

admin.site.register(Announcements)
admin.site.register(Syllabus)
admin.site.register(Calendar)
admin.site.register(Questionp)