from django.conf.urls import patterns, include, url
import core.views as cv

urlpatterns = patterns('',
    url(r'^$', cv.LandingView.as_view(), name="landing"),
    url(r'locations/', cv.LocationListView.as_view(), name="location_list"),
    url(r'location/(?P<pk>\d+)/detail/$', cv.LocationDetailView.as_view(), name='location_detail'),
)


