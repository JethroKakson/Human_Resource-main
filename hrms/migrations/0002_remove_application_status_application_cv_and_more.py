# Generated by Django 4.2.2 on 2023-06-16 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='status',
        ),
        migrations.AddField(
            model_name='application',
            name='cv',
            field=models.ImageField(default='empty', height_field=500, upload_to='', verbose_name='CV', width_field=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp953', max_length=70),
        ),
    ]