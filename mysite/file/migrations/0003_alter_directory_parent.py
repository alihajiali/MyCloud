# Generated by Django 4.0.4 on 2022-05-05 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_directory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='file.directory'),
        ),
    ]
