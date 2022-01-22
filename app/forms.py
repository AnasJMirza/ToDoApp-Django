from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from app.models import TODO

class TODOForm(ModelForm):
    class Meta:
        model = TODO
        fields = ['title', 'status', 'priority']