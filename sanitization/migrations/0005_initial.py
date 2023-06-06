# Generated by Django 3.2.12 on 2022-02-15 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sanitization', '0004_auto_20220215_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestID', models.CharField(max_length=50, null=True)),
                ('DateofSanitization', models.DateField(null=True)),
                ('TimeofSanitization', models.TimeField(null=True)),
                ('Address', models.CharField(max_length=250, null=True)),
                ('MobileNumber', models.CharField(max_length=15, null=True)),
                ('State', models.CharField(max_length=150, null=True)),
                ('City', models.CharField(max_length=150, null=True)),
                ('Message', models.CharField(max_length=350, null=True)),
                ('RequestDate', models.DateTimeField(auto_now_add=True)),
                ('Remark', models.CharField(max_length=250, null=True)),
                ('Status', models.CharField(max_length=100, null=True)),
                ('UpdationDate', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=250, null=True)),
                ('Price', models.CharField(max_length=200, null=True)),
                ('Image', models.FileField(max_length=150, null=True, upload_to='')),
                ('ServiceDetail', models.CharField(max_length=350, null=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Remark', models.CharField(max_length=350, null=True)),
                ('Status', models.CharField(max_length=100, null=True)),
                ('UpdationDate', models.DateTimeField(auto_now_add=True)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanitization.requests')),
            ],
        ),
        migrations.AddField(
            model_name='requests',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanitization.services'),
        ),
        migrations.AddField(
            model_name='requests',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]