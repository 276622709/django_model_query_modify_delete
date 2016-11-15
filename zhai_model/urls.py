from django.conf.urls import patterns, include, url
from testmodel.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zhai_model.views.home', name='home'),
    # url(r'^zhai_model/', include('zhai_model.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

        
        url(r'^beginAdd/$',beginAdd),
        url(r'^add$',add),
	url(r'^q$',query),
	url(r'^index.html$',beginAdd),
	url(r'delete$',delByID),

	url(r'showid$',showUid),
)
