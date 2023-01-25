# Generated by Django 3.2.9 on 2023-01-25 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('division', models.CharField(blank=True, choices=[('GOKART', 'Gokart'), ('EV', 'Electric Vehicle')], max_length=200, null=True)),
                ('image', models.ImageField(null=True, upload_to='UIMS/Sponsors')),
            ],
        ),
    ]