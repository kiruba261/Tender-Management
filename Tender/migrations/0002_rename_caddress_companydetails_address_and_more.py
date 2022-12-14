# Generated by Django 4.0 on 2022-08-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tender', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydetails',
            old_name='CAddress',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='companydetails',
            old_name='CDetails',
            new_name='Company_Details',
        ),
        migrations.RenameField(
            model_name='companydetails',
            old_name='CGst',
            new_name='Company_Name',
        ),
        migrations.RenameField(
            model_name='companydetails',
            old_name='cQuote',
            new_name='Company_Quote',
        ),
        migrations.RenameField(
            model_name='companydetails',
            old_name='CType',
            new_name='Company_Type',
        ),
        migrations.RenameField(
            model_name='companydetails',
            old_name='CPAN',
            new_name='PAN',
        ),
        migrations.RemoveField(
            model_name='companydetails',
            name='CName',
        ),
        migrations.AddField(
            model_name='companydetails',
            name='GST',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
