from django.conf.urls import patterns, include, url
import core.views as cv

urlpatterns = patterns('',
    url(r'^$', cv.LandingView.as_view(), name="landing"),
    url(r'api/location/$', cv.LocationAPIView.as_view(), name="api_location_list"),
    url(r'api/location/(?P<pk>\d+)/detail/$', cv.LocationAPIView.as_view(), name="api_location_detail"),
    url(r'location/$', cv.LocationListView.as_view(), name="location_list"),
    url(r'location/(?P<pk>\d+)/detail/$', cv.LocationDetailView.as_view(), name='location_detail'),

)


