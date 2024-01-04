# Generated by Django 5.0 on 2024-01-01 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyers', '0003_category_lawyer_experience_lawyer_office_location_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawyer',
            name='document',
        ),
        migrations.RemoveField(
            model_name='lawyer',
            name='registrationDate',
        ),
        migrations.AddField(
            model_name='lawyer',
            name='fax',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AddField(
            model_name='lawyer',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]