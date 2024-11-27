from django.contrib import admin
from .models import order,ordereditem

# Register your models here.
class orderadmin(admin.ModelAdmin):
    list_filter = [
        "owner",
        "order_status"
    ]
    search_fields = [
        "owner",
        "id"
    ]

admin.site.register(order,orderadmin)


