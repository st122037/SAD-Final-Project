from django.contrib import admin

# Register your models here.
from django.contrib import admin
from reminder_app.models import Reminder, User

admin.site.register(User)
admin.site.register(Reminder)