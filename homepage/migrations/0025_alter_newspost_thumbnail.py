# Generated by Django 3.2.9 on 2022-11-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0024_delete_teammember'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='UIMS'),
        ),
    ]
