from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'administracion'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^new$', views.invoiceSelectProviderView, name='invoice_new'),
    url(r'^delete/(?P<pk>\d+)$', views.invoice_delete, name='invoice_delete'),
    url(r'^ajax/print_message/$', views.print_message, name='print_message'),
    url(r'^ajax/get_order_details/$', views.get_order_details, name='get_order_details'),
    path('invoice', views.invoice, name='invoice'),
    path('name', views.get_name, name='name'),
    path('your-name', views.yourname, name='yname'),
    path('invoice_select_provider', views.invoiceSelectProviderView, name='invoiceSelectProvider'),
    path('invoice_select_order', views.invoiceSelectOrderView, name='invoiceSelectOrder'),
    #path('invoice_form', views.invoice_create, name='invoice_create'),
    path('create', views.InvoiceCreateView.as_view(), name='invoice_create'),
]