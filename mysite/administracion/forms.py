from django import forms
from .models import Provider, Order, Invoice, InvoiceDetail, OrderDetail
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from crispy_forms.layout import Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *


"""
# Clase InvoiceForm perteneciente a la version estable 1.0 Descomentar en caso de ser necesario.
class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ('invoice_num', 'order', 'period',)

    def __init__(self, orden, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        print('InvoiceForm order: ', self.fields['order'])
        self.fields['order'].initial = orden
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('invoice_num', css_class='form-group col-md-6 mb-0'),
                Column('order', css_class='form-group col-md-4 mb-0'),
                Column('period', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            )
        )
"""

class InvoiceForm2(ModelForm):
    class Meta:
        model = Invoice
        fields = ('invoice_num', 'order', 'period',)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    invoice = forms.ModelChoiceField(label='Select an invoice', queryset=Invoice.objects.all())

"""
# Clase InvoiceDetailForm perteneciente a la version estable 1.0 Descomentar en caso de ser necesario.
class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = ('invoice', 'invoice_row', 'order_row', 'invoice_row_qty', )

    def __init__(self, invoice, *args, **kwargs):
        super(InvoiceDetailForm, self).__init__(*args, **kwargs)
        self.fields['invoice_row'].queryset = InvoiceDetail.objects.filter(invoice=invoice)
"""
# Clase destinada a manipular facturas.
class InvoiceSelectProviderForm(forms.ModelForm):
    class Meta:
#        model = Provider
#        fields = ('provider_denomination', )
        model = Order
        fields = ('provider', )

class InvoiceSelectOrderForm3(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('provider', 'order_num', )

    def __init__(self, prov, *args, **kwargs):
        super(InvoiceSelectOrderForm3, self).__init__(*args, **kwargs)
        print('prov:', prov)
        self.fields['order_num'].queryset = Order.objects.filter(provider=prov)
        print('filter: ', self.fields['order_num'].queryset)
        print(self)

class InvoiceSelectOrderForm(forms.Form):
    provider = forms.CharField(max_length=20)
    order_num = forms.ModelChoiceField(queryset=Order.objects.all())

    def __init__(self, prov, *args, **kwargs):
        super(InvoiceSelectOrderForm, self).__init__(*args, **kwargs)
        print('prov:', prov)
        self.fields['order_num'].queryset = Order.objects.filter(provider=prov)
        self.fields['provider'].disabled = True
        print('filter: ', self.fields['order_num'].queryset)
        print(self)


# Probando Vistas Basadas en Clases.

class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        exclude = ()
        
    def __init__(self, *args, **kwargs):
        super(InvoiceDetailForm, self).__init__(*args, **kwargs)
        self.fields['order_row'].queryset = OrderDetail.objects.none()

InvoiceDetailFormSet = inlineformset_factory(
    Invoice, InvoiceDetail, form=InvoiceDetailForm, fields=['invoice_row', 'order_row', 'invoice_row_qty'],
    extra=1, can_delete=True
    )

class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('invoice_num'),
                Field('order'),
                Field('period'),
                Fieldset('Agregar filas de factura',
                    Formset('details')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )
