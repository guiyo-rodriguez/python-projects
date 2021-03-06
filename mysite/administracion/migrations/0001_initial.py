# Generated by Django 2.2.1 on 2019-06-17 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_num', models.CharField(max_length=20, verbose_name='Ident. de Factura')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=20, verbose_name='Ident. de OC')),
                ('osi', models.CharField(max_length=6, verbose_name='Ident. OC interno')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_denomination', models.CharField(max_length=6, verbose_name='Periodo')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_denomination', models.CharField(max_length=60, verbose_name='Razon social')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_row', models.IntegerField(default=1)),
                ('order_row_qty', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('order_row_unit_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Precio unit.')),
                ('order_row_item', models.CharField(max_length=40, verbose_name='Item')),
                ('valid_from_date', models.DateField(verbose_name='Desde')),
                ('valid_to_date', models.DateField(verbose_name='Hasta')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderdetails', to='administracion.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Provider'),
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_row', models.IntegerField(default=1)),
                ('invoice_row_qty', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Cantidad')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Invoice')),
                ('order_row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.OrderDetail')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Order'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Period'),
        ),
    ]
