# Generated by Django 3.2.9 on 2023-01-25 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0026_alter_newspost_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='UIMS/homepage_banner')),
            ],
        ),
    ]
