# Generated by Django 3.1.6 on 2022-04-07 21:19

import application.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0007_auto_20220407_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('order_category', models.CharField(max_length=200)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['order_category'],
            },
        ),
        migrations.CreateModel(
            name='Order_Document',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('document_number', models.CharField(default='00', max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('remarks', models.CharField(blank=True, default='None', max_length=5000, null=True)),
                ('file', models.FileField(upload_to='order/', validators=[application.validators.validate_file_extension])),
                ('date_signed', models.DateField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('order_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.order_category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_signed', 'description'],
            },
        ),
    ]
