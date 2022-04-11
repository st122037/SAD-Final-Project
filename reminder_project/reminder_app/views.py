from django.shortcuts import render
from django.views.generic import ListView
from .models import Reminder

# Create your views here.
class ReminderView(ListView):
    model = Reminder
    template_name = "reminder.html"

    def get_queryset(self):
        result = [o for o in Reminder.objects.filter() if "CreaThor" in o.access_rights["editors"]]
        return result