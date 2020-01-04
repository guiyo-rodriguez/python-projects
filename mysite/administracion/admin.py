from django.contrib import admin
#from django.conf.locale.es import formats as es_formats

# Register your models here.

from .models import OrderDetail, Order, Period, Invoice, InvoiceDetail, Provider

#es_formats.DATETIME_FORMAT = "d M Y"

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail

class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['order_num', 'osi']}),
        ('Datos del Proveedor', {'fields': ['provider']}),
    ]
    inlines = [OrderDetailInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(Period)

class InvoiceDetailInline(admin.TabularInline):
    model = InvoiceDetail

class InvoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['invoice_num', 'order', 'period']}),
    ]
    inlines = [InvoiceDetailInline]
    list_display = ('invoice_num', 'period', 'order', 'provider')

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceDetail)
admin.site.register(Provider)