from django.db import models
from django.db.models import Model, ForeignKey
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
import uuid
from application.validators import validate_file_extension

class Incoming_Category(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    incoming_category       = models.CharField(max_length = 200)
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.incoming_category)

    class Meta:
        ordering = ['incoming_category']

class Outgoing_Category(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    outgoing_category       = models.CharField(max_length = 200)
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.outgoing_category)

    class Meta:
        ordering = ['outgoing_category']

class Order_Category(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_category          = models.CharField(max_length = 200)
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.order_category)

    class Meta:
        ordering = ['order_category']

class Ordinance_Resolution_Category(models.Model):
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


class Incoming_Document(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    incoming_category       = models.ForeignKey(Incoming_Category, on_delete = models.CASCADE)
    series_no               = models.CharField(default="00",max_length = 200,blank=True,null=True)
    remarks                 = models.CharField(default="None",max_length = 5000,blank=True,null=True)
    description             = models.CharField(max_length = 5000)
    file                    = models.FileField(upload_to='incoming/', validators=[validate_file_extension])
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    date_received           = models.DateField(default=timezone.now)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering = ['date_received','description']


class Outgoing_Document(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    outgoing_category       = models.ForeignKey(Outgoing_Category, on_delete = models.CASCADE)
    description             = models.CharField(max_length = 5000)
    remarks                 = models.CharField(default="None",max_length = 5000,blank=True,null=True)
    file                    = models.FileField(upload_to='outgoing/', validators=[validate_file_extension])
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    date_issued             = models.DateField(default=timezone.now)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering = ['date_issued','description']

class Order_Document(models.Model):
    id                      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document_number         = models.CharField(default="00",max_length = 200)
    order_category          = models.ForeignKey(Order_Category, on_delete = models.CASCADE)
    description             = models.CharField(max_length = 5000)
    remarks                 = models.CharField(default="None",max_length = 5000,blank=True,null=True)
    file                    = models.FileField(upload_to='order/', validators=[validate_file_extension])
    user                    = models.ForeignKey(User, on_delete = models.CASCADE)
    date_signed             = models.DateField(default=timezone.now)
    date_updated            = models.DateTimeField(auto_now = True)
    date_created            = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering = ['date_signed','description']


class Ordinance_Resolution_Document(models.Model):
    id                                     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document_number                        = models.CharField(default="00",max_length = 200)
    category          = models.ForeignKey(Ordinance_Resolution_Category, on_delete = models.CASCADE)
    description                            = models.CharField(max_length = 5000)
    remarks                                = models.CharField(default="None",max_length = 5000,blank=True,null=True)
    file                                   = models.FileField(upload_to='order/', validators=[validate_file_extension])
    user                                   = models.ForeignKey(User, on_delete = models.CASCADE)
    date_approved                          = models.DateField(default=timezone.now)
    date_updated                           = models.DateTimeField(auto_now = True)
    date_created                           = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.description)

    class Meta:
        ordering = ['date_approved','description']
