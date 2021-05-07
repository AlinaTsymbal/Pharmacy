# Generated by Django 3.2 on 2021-05-07 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedKit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'med_kit',
            },
        ),
        migrations.AddField(
            model_name='remedy',
            name='med_kits',
            field=models.ManyToManyField(db_table='med_kit_remedy', related_name='remedies', to='api.MedKit'),
        ),
    ]
