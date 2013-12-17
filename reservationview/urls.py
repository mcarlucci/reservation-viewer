from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from reservations import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reservations', views.ReservationViewSet)

urlpatterns = patterns('',
    url(r'^$', views.reservation_gallery, name='reservations_gallery'),

    url(r'^api/', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
)
