from django.contrib import admin

# Register your models here.
from application.models import (
    Incoming_Category,
    Outgoing_Category,
    Order_Category,
)


admin.site.register(Incoming_Category)
admin.site.register(Outgoing_Category)
admin.site.register(Order_Category)
