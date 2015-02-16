from django import forms
import core.models as cm
from django.contrib.auth.models import User
import django.forms.extras.widgets as widgets

class SearchForm(forms.Form):
    query = forms.CharField(max_length=500)