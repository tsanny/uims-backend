# Generated by Django 4.0.6 on 2022-07-26 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_alter_teamrole_division_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamrole',
            name='division_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Division/Director name'),
        ),
    ]
