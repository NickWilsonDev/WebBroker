from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webbroker.views.home', name='home'),
# front end urls
    url(r'^$', 'loads.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'loads.views.user_login', name='login'),
    url(r'^logout/$', 'loads.views.user_logout', name='logout'),    
    url(r'^about/$', 'loads.views.about', name='about'),
    url(r'^customerContact/$', 'loads.views.customerContact', name='customerContact'),
    url(r'^carrierContact/$', 'loads.views.carrierContact', name='carrierContact'),
    url(r'^missionStatement/$', 'loads.views.missionStatement', name='missionStatement'),

# back end urls
    url(r'^newCustomer/$', 'customers.views.newCustomer', name='newCustomer'),
    url(r'^customerList/$', 'customers.views.listCustomers', name='listCustomers'),
    url(r'^customerEdit/(?P<pk>[0-9]+)$', 'customers.views.customerEdit', name='customerEdit'),
    url(r'^customerDetail/(?P<pk>[0-9]+)/$', 'customers.views.customerDetail', name='customerDetail'),

    url(r'^newCarrier/$', 'carriers.views.newCarrier', name='newCarrier'),
    url(r'^carrierList/$', 'carriers.views.listCarriers', name='listCarriers'),
    url(r'^carrierDetail/(?P<pk>[0-9]+)/$', 'carriers.views.carrierDetail', name='carrierDetail'),    
    url(r'^carrierEdit/(?P<pk>[0-9]+)$', 'carriers.views.carrierEdit', name='carrierEdit'),
    
    url(r'^newLoad/$', 'loads.views.newLoad', name='newLoads'),
    url(r'^listLoads/$', 'loads.views.listLoads', name='listLoads'),
    url(r'^loadDetail/(?P<pk>[0-9]+)/$', 'loads.views.loadDetail', name='loadDetail'),
    url(r'^loadEdit/(?P<pk>[0-9]+)$', 'loads.views.loadEdit', name='loadEdit'),
    url(r'^loadDelete/(?P<pk>[0-9]+)$', 'loads.views.loadDelete', name='loadDelete'),
    url(r'^loadConfirmation/(?P<pk>[0-9]+)$', 'loads.views.loadConfirm', name='loadConfirm'),
    url(r'^home/$', 'loads.views.home', name='home'),

)
