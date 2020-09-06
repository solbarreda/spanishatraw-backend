# Generated by Django 3.1 on 2020-09-06 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_service_description'),
        ('payment', '0005_auto_20200902_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='service',
        ),
        migrations.AddField(
            model_name='invoice',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='services.service', verbose_name='Invoice'),
            preserve_default=False,
        ),
    ]
