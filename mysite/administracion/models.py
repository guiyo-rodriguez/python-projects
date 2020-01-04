from django.db import models


class Provider(models.Model):
    provider_denomination = models.CharField('Razon social', max_length=60)
    def __str__(self):
        return self.provider_denomination

class Period(models.Model):
    period_denomination = models.CharField('Periodo', max_length=6)
    def __str__(self):
        return self.period_denomination

class Order(models.Model):
    order_num = models.CharField('Ident. de OC', max_length=20)
    osi = models.CharField('Ident. OC interno', max_length=6)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_num

    def provider_denom(self):
        return self.provider.provider_denomination

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderdetails')
    order_row = models.IntegerField(default=1)
    order_row_qty = models.IntegerField('Cantidad', default=0)
    order_row_unit_price = models.DecimalField('Precio unit.', max_digits=12, decimal_places=2)
    order_row_item = models.CharField('Item', max_length=40)
    valid_from_date = models.DateField('Desde')
    valid_to_date = models.DateField('Hasta')

    def __str__(self):
        return str(self.order_row) + "-" + self.order.order_num

class Invoice(models.Model):
    invoice_num = models.CharField('Ident. de Factura', max_length=20)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

    def __str__(self):
        return self.invoice_num

    def provider(self):
        return self.order.provider

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="has_details", on_delete=models.CASCADE)
    invoice_row = models.IntegerField(default=1)
    order_row = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    invoice_row_qty = models.DecimalField('Cantidad', max_digits=8, decimal_places=2)

    def __str__(self):
        return str(self.invoice_row)
    
    def unit_price(self):
        return str(self.order_row.order_row_unit_price)