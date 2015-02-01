from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.shortcuts import render
from sitegate.decorators import redirect_signedin, sitegate_view
import core.models as cm
import core.forms as cf
import decimal
import json

# Create your views here.

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)

class LandingView(TemplateView):
    template_name = 'base/index.html'

class LocationListView(ListView):
    template_name = 'location/list.html'
    model = cm.Location
    paginate_by = 5

class LocationAPIView(TemplateView):
    template_name = 'location/list.html'

    def get_context_data(self, **kwargs):
        context = super(LocationAPIView, self).get_context_data(**kwargs)
        output = []
        if 'pk' in self.kwargs:
            locations = cm.Location.objects.filter(id=self.kwargs['pk'])
        else:
            locations = cm.Location.objects.all()

        for l in locations:
            blob = {
                'id':l.id,
                'lattitude':l.position.latitude,
                'longitude':l.position.longitude,
                'title':l.title,
            }
            output.append(blob)
        context['locations'] = output
        return context

    def get(self, request, *args, **kwargs):
        supes = super(LocationAPIView, self).get(request, *args, **kwargs)
        context = self.get_context_data(**kwargs)
        data = json.dumps(context, default=decimal_default)
        out_kwargs = {'content_type':'application/json'}
        return HttpResponse(data, **out_kwargs)

        return supes

class LocationDetailView(TemplateView):
    template_name = 'location/detail.html'

    def get_context_data(self, **kwargs):

        # Call the base implementation first to get a context
        context = super(LocationDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        location = cm.Location.objects.get(id=self.kwargs['pk'])
        user_review = None
        if self.request.user.is_authenticated():
            reviews = location.review_set.exclude(user=self.request.user)
            user_reviews = cm.Review.objects.filter(user=self.request.user, location=location)
            if user_reviews.count() > 0:
                user_review = user_reviews[0]
        else:
            reviews = location.review_set.all()
        

        context['location'] = location
        context['reviews'] = reviews
        context['user_review'] = user_review
        return context

class LocationCreateView(CreateView):
    model = cm.Location
    template_name = 'base/form.html'
    form_class = cf.LocationForm

class LocationUpdateView(UpdateView):
    model = cm.Location
    template_name = 'base/form.html'
    form_class = cf.LocationForm

class ReviewCreateView(CreateView):
    model = cm.Review
    template_name = 'base/form.html'
    form_class = cf.ReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.location = cm.Location.objects.get(id=self.kwargs['pk'])
        return super(ReviewCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.location.get_absolute_url()

class ReviewUpdateView(UpdateView):
    model = cm.Review
    template_name = 'base/form.html'
    form_class = cf.ReviewForm

    def get_object(self):
        return cm.Review.objects.get(location__id=self.kwargs['pk'], user=self.request.user)

    def get_success_url(self):
        return self.object.location.get_absolute_url()

class SearchView(ListView):
    template_name = 'location/list.html'
    model = cm.Location
    paginate_by = 5

    def get_queryset(self):
        return cm.Location.objects.filter(title__icontains=self.request.GET.get('query', ''))
        


@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3')  # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
    return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})