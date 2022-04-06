from django.db import models
from django.db.models import Model, ForeignKey
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
import uuid
from application.validators import validate_file_extension

class Category(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category                = models.CharField(max_length = 200)
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.category)

    class Meta:
        ordering = ['category']

class Year(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year                    = models.CharField(max_length = 200)
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.year)

    class Meta:
        ordering = ['year']


class Document(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category                = models.ForeignKey(Category, on_delete = models.CASCADE)
    year                    = models.ForeignKey(Year, on_delete = models.CASCADE)
    series_no               = models.CharField(default="00",max_length = 200,blank=True,null=True)
    remarks                 = models.CharField(default="None",max_length = 5000,blank=True,null=True)
    description             = models.CharField(max_length = 5000)
    file                    = models.FileField(upload_to='upload_document/', validators=[validate_file_extension])
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering = ['year','description']
