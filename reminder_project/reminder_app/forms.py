from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
        options = (
        ('not started', 'Not Started'),
        ('in progress', 'In Progress'),
        ('finished', 'Finished'))

        priority = ( ('high', 'High'),
                    ('medium', 'Medium'),
                    ('low', 'Low')) 


        reminder_id = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width:550px; height:40px;'}))
        title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','style': 'width:550px; height:40px;'}))
        status = forms.CharField(widget=forms.Select(choices=options, attrs={'class': 'form-control','style': 'width:550px; height:40px;'}))
        priority = forms.CharField(widget=forms.Select(choices=priority, attrs={'class': 'form-control','style': 'width:550px; height:40px;'}))
        description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','style': 'width:550px; height:170px;'}))
        tags = forms.JSONField(widget=forms.Textarea(attrs={'class': 'form-control','style': 'width:550px; height:100px;'}))
        editors = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','style': 'width:550px; height:100px;'}))
        viewers = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','style': 'width:550px; height:100px;'}))

        created_date = forms.DateField(widget=forms.SelectDateWidget)
        due_date = forms.DateTimeField(widget=forms.SelectDateWidget)
    
        class Meta:
            model = Reminder
            fields = ['reminder_id', 'title', 'status', 'priority','description','tags']