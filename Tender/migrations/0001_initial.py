# Generated by Django 4.0 on 2022-08-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companydetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CName', models.CharField(max_length=50)),
                ('CType', models.CharField(max_length=20)),
                ('CAddress', models.CharField(max_length=50)),
                ('CGst', models.CharField(max_length=25)),
                ('CPAN', models.CharField(max_length=10)),
                ('CDetails', models.CharField(max_length=70)),
                ('cQuote', models.FileField(upload_to='')),
                ('dateposted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]