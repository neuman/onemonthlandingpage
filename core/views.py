from django.shortcuts import render
from django.views.generic.base import TemplateView
import core.models as cm

# Create your views here.

class LandingView(TemplateView):
    template_name = 'base/index.html'

class LocationListView(TemplateView):
    template_name = 'location/list.html'

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(LocationListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['locations'] = cm.Location.objects.all().order_by('created_at')
        return context

class LocationDetailView(TemplateView):
    template_name = 'location/detail.html'

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(LocationDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['location'] = cm.Location.objects.get(id=self.kwargs['pk'])
        return context