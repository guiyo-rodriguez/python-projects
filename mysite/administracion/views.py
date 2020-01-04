from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.forms import modelformset_factory, modelform_factory
from django.forms.models import inlineformset_factory
from .models import Invoice, Provider, Order, InvoiceDetail
from .forms import NameForm, InvoiceDetailForm, InvoiceSelectProviderForm, InvoiceSelectOrderForm, InvoiceForm, InvoiceForm2, InvoiceDetailFormSet
from django.views.generic.edit import CreateView, UpdateView
from crispy_forms.helper import FormHelper, Layout
from django.http import JsonResponse
#from builtins import None
from django.db import transaction
from django.urls import reverse_lazy
from msilib.schema import ODBCAttribute


def print_message(request):
    invoice_num = request.GET.get('invoice_num', None)
    print("FACTURA: ", invoice_num)
    data = {
        'message': "La factura es " + invoice_num
    }
    return JsonResponse(data)

def get_order_details(request):
    order_num = request.GET.get('order_num', None)
    print("get_order_details.order_num: ", order_num)
    order = get_object_or_404(Order, pk=order_num)
    print("get_order_details.order: ", order)
    
    #data = {
    #    'order_rows': order.orderdetails.all()
    #}
    
    print("get_order_details.data: ", list(order.orderdetails.all().values()))
    data = dict()
    odr = list()
    
    for od in list(order.orderdetails.all().values()):
        odr.append({k:od[k] for k in ('order_row', 'order_row_item', 'order_row_qty') if k in od})
        print({k:od[k] for k in ('order_row','order_row_item','order_row_qty') if k in od})
    
    print("-> ", odr)
    
    data['orderdetails'] = odr
    
    return JsonResponse(data)
    

def home(request, template_name='administracion/home.html'):
    invoices = Invoice.objects.all()
    ctx = {}
    ctx['invoices'] = invoices
    return render(request, template_name, ctx)

class InvoiceCreateFormsetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(InvoiceCreateFormsetHelper, self).__init__(*args, **kwargs)
        self.layout = Layout(
            'invoice_row', 
            'order_row', 
            'invoice_row_qty'
        )
        self.template = 'bootstrap/table_inline_formset.html'

def invoice_create(request, template_name='administracion/invoice_form.html'):
    print("Ingresa a invoice_create")
    if request.method == 'POST':
        print("Ingresa a invoice_create POST")
        InlineFormSet = inlineformset_factory(Invoice, InvoiceDetail, fields=('invoice_row', 'order_row', 'invoice_row_qty'))
        form = InvoiceForm2(request.POST or None)
        formset = InlineFormSet(request.POST or None, instance=Invoice())
        if form.is_valid() and formset.is_valid():
            invoice = form.save()
            formset.instance = invoice
            formset.save()
            return redirect('administracion:home')
    else:
        print("Ingresa a invoice_create GET")
        order = get_object_or_404(Order, pk=request.GET.get('order_num'))
        InlineFormSet = inlineformset_factory(Invoice, InvoiceDetail, fields=('invoice_row', 'order_row', 'invoice_row_qty'))
        form = InvoiceForm(orden=order)
        invoice = Invoice()
        formset = InlineFormSet(request.POST or None, instance=invoice)

        for f in formset:
            f.fields['order_row'].queryset = order.orderdetails.all()

    FormHelper.form_tag = False
    helper = InvoiceCreateFormsetHelper()
    ctx = {}
    ctx['form'] = form
    ctx['formset'] = formset
    ctx['helper'] = helper
    return render(request, template_name, ctx)

def invoice_delete(request, pk, template_name='administracion/invoice_confirm_delete.html'):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method=='POST':
        invoice.delete()
        return redirect('administracion:home')
    ctx = {}
    ctx['invoice'] = invoice
    return render(request, template_name, ctx)



def invoice(request):
    invoice_list = Invoice.objects.all()
    paginator = Paginator(invoice_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    invoices = paginator.get_page(page)
    return render(request, 'administracion/invoice.html', {'invoices': invoices})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'administracion/name.html', {'form': form})

def yourname(request):
    saludo = "Hola!"
    nombre = request.POST.get('your_name')
    saludo = "Hola " + nombre + "!"
    #invoice = request.POST.get('invoice')
    invoice = get_object_or_404(Invoice, pk=request.POST.get('invoice'))
    comentario = "Seleccionaste la factura " + invoice.invoice_num + " del proveedor " + invoice.provider().provider_denomination
    #form_det = InvoiceDetailForm(request.POST.get('invoice'))
    InvoiceDetailFormSet = modelformset_factory(InvoiceDetail, fields = ('invoice_row', 'order_row', 'invoice_row_qty'), extra=0)
    data = request.POST or None
    #form_det = InvoiceDetailFormSet(data=data, queryset=InvoiceDetail.objects.filter(invoice=invoice))
    #form_det = InvoiceDetailFormSet()
    form_det = InvoiceDetailFormSet(queryset=InvoiceDetail.objects.filter(invoice=invoice))
    return render(request, 'administracion/hola.html', {'salu': saludo, 'com': comentario, 'formulario': form_det})
   
def invoiceSelectProviderView(request):
    form = InvoiceSelectProviderForm()
    return render(request, 'administracion/invoice_select_provider.html', {'form': form})

def invoiceSelectOrderView(request):
    if request.method == 'POST':
        provider = get_object_or_404(Provider, pk=request.POST.get('provider'))
        provider_pk = request.POST.get('provider')
        print("El proveedor es: ", provider, " su pk es: ", provider_pk)
        #form = InvoiceSelectOrderForm(prov=provider, initial={'provider': provider})
        form = InvoiceSelectOrderForm(prov=provider, initial={'provider': provider})
        #form.provider = provider
#       if form.is_valid():
        return render(request, 'administracion/invoice_select_order.html', {'form': form})
    return HttpResponseRedirect('/thanks/')


# Probando Vistas Basadas en Clases y creacion dinamica de formsets.

class InvoiceCreateView(CreateView):
    model = Invoice
    template_name = 'administracion/invoice_create.html'
    form_class = InvoiceForm
    success_url = None
    print("paso por InvoiceCreate")
    
    def get_context_data(self, **kwargs):
        print("paso por get_context_data 1")
        data = super(InvoiceCreateView, self).get_context_data(**kwargs)
        print("paso por get_context_data 2")
        if self.request.POST:
            data['details'] = InvoiceDetailFormSet(self.request.POST)
        else:
            data['details'] = InvoiceDetailFormSet()
            print("data['details']=", data['details'])
        
        return data
    
    def form_valid(self, form):
        
        context = self.get_context_data()
        details = context['details']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if details.is_valid():
                details.instance = self.object
                details.save()

        return super(InvoiceCreateView, self).form_valid(form)
        #return CreateView.form_valid(self, form)

    def get_success_url(self):
        return reverse_lazy('administracion:home')
        #return reverse_lazy('administracion:home', kwargs={'pk': self.object.pk})
        #return CreateView.get_success_url(self)