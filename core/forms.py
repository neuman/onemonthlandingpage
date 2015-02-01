from django import forms
import core.models as cm
from django.contrib.auth.models import User
import django.forms.extras.widgets as widgets


class BootstrapForm(forms.ModelForm):
    exclude = ['changed_by']
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.attrs.has_key('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs.update({'class':'form-control'})

class LocationForm(BootstrapForm):
    class Meta:
        model = cm.Location
        exclude = ['created_at']

class ReviewForm(BootstrapForm):
    class Meta:
        model = cm.Review
        exclude = ['location', 'created_at','user']

class SearchForm(forms.Form):
    query = forms.CharField(max_length=500)