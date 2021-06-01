# Generated by Django 3.2 on 2021-06-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_order_orderremedy'),
    ]

    operations = [
        migrations.AddField(
            model_name='remedy',
            name='application_method',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='remedy',
            name='contraindication',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='remedy',
            name='form',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='remedy',
            name='group',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='remedy',
            name='indication',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='remedy',
            name='manufacturer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='remedy',
            name='side_effects',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='remedy',
            name='structure',
            field=models.TextField(blank=True, null=True),
        ),
    ]