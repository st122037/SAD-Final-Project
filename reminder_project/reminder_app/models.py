from django.db import models
# Create your models here.


def generate_accesses():
    d = dict()
    d['editors'] = []
    d['viewers'] = []
    return d

def create_public_url(id):
	pass

class Reminder(models.Model):
    reminder_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=15, default="not started") # not started, in progress, done
    priority = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    tags = models.JSONField(default=list, blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True)


    access_rights = models.JSONField(default=generate_accesses)
    public_url = models.URLField(blank=True)
    public_url_can_edit = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}: due {self.due_date}"


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    has_logged_out = models.BooleanField(default=True)  # if true, the user needs to log in again, which sets this field to false. If false, the JWT token is still valid. 

    def __str__(self):
        return self.user_id