from django.shortcuts import render,redirect, get_object_or_404
# from django.views.generic import ListView
from .models import Reminder
from .forms import ReminderForm


def index(request):
    context = Reminder.objects.all()
    return render(request, 'reminder/reminder.html', {'context': context})

# class ReminderView(ListView):
#     model = Reminder
#     # template_name = "reminder.html"

def get_queryset(self):
        result = [o for o in Reminder.objects.filter() if "CreaThor" in o.access_rights["editors"]]
        return result


def create_reminder(request):
    template = 'reminder/create_reminder.html'
    form = ReminderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, template, context)

def edit_reminder(request, pk):
    template = 'reminder/edit_reminder.html'
    reminder = get_object_or_404(Reminder, pk=pk)
    form = ReminderForm(request.POST or None, instance=reminder)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, template, context)

def delete_reminder(request, pk):
    template = 'reminder/delete_reminder.html'
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        reminder.delete()
        return redirect('/')
    context = {"reminder": reminder}
    return render(request, template, context)