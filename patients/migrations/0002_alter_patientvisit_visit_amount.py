# Generated by Django 4.0.5 on 2022-07-22 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientvisit',
            name='visit_amount',
            field=models.IntegerField(null=True),
        ),
    ]
