# Generated by Django 5.0 on 2023-12-20 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ThejsonCruderApp', '0010_jsondata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jsondata',
            name='table_data',
        ),
        migrations.AddField(
            model_name='jsondata',
            name='json_file',
            field=models.FileField(default='No values', upload_to='json_files/'),
        ),
    ]
