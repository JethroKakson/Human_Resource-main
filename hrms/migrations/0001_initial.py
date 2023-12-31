# Generated by Django 4.2.2 on 2023-06-15 17:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(default='location', max_length=70)),
                ('history', models.TextField(blank=True, default='No History', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(default='emp325', max_length=70)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('job_title', models.CharField(default='Job Title', max_length=20)),
                ('dob', models.DateTimeField()),
                ('mobile', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=125)),
                ('address', models.TextField(default='', max_length=100)),
                ('emergency', models.CharField(max_length=11)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=10)),
                ('joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('luganda', 'LUGANDA')], default='english', max_length=10)),
                ('account_no', models.CharField(default='0123456789', max_length=10)),
                ('bank', models.CharField(default='First Bank Plc', max_length=25)),
                ('salary', models.CharField(default='00,000.00', max_length=16)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrms.department')),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('position', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=25)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_period_start', models.DateField()),
                ('pay_period_end', models.DateField()),
                ('gross_pay', models.DecimalField(decimal_places=2, max_digits=8)),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=8)),
                ('deductions', models.DecimalField(decimal_places=2, max_digits=8)),
                ('net_pay', models.DecimalField(decimal_places=2, max_digits=8)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrms.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.CharField(max_length=15)),
                ('end', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('approved', 'APPROVED'), ('unapproved', 'UNAPPROVED'), ('decline', 'DECLINED')], default='Not Approved', max_length=15)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hrms.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Kin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=100)),
                ('occupation', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=14)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hrms.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('first_in', models.TimeField()),
                ('last_out', models.TimeField(null=True)),
                ('status', models.CharField(choices=[('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'), ('UNAVAILABLE', 'UNAVAILABLE')], max_length=15)),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hrms.employee')),
            ],
        ),
    ]
