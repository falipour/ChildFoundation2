# Generated by Django 2.0 on 2018-02-02 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hamyar', '0003_paymentfoundation'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='hamyar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='hamyar.Hamyar'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentfoundation',
            name='hamyar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='hamyar.Hamyar'),
            preserve_default=False,
        ),
    ]
