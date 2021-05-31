# Generated by Django 3.2 on 2021-05-20 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_remedy_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remedy',
            name='pharmacies',
        ),
        migrations.CreateModel(
            name='PharmacyRemedy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.TextField(blank=True, null=True)),
                ('pharmacy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.pharmacy')),
                ('remedy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.remedy')),
            ],
            options={
                'db_table': 'pharmacy_remedy',
            },
        ),
    ]