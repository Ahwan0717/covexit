# Generated by Django 2.2.12 on 2020-04-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0006_add_forked_partner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partneraddress',
            options={'verbose_name': 'address', 'verbose_name_plural': 'addresses'},
        ),
        migrations.AddField(
            model_name='partneraddress',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='is main address'),
        ),
        migrations.AddField(
            model_name='partneraddress',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9, verbose_name='latitude'),
        ),
        migrations.AddField(
            model_name='partneraddress',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9, verbose_name='longitude'),
        ),
        migrations.AddField(
            model_name='partneraddress',
            name='mail',
            field=models.EmailField(default='', max_length=80, verbose_name='e-mail address'),
        ),
        migrations.AddField(
            model_name='partneraddress',
            name='phone',
            field=models.CharField(default='', max_length=45, verbose_name='phone'),
        ),
        migrations.AddField(
            model_name='partneraddress',
            name='website',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='website'),
        ),
    ]
