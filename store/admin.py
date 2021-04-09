from django.contrib import admin
from .models import Plane


admin.site.site_header = "Fiery Sky Admin"
admin.site.index_title = "Fiery Sky"
admin.site.site_title = "Admin"
@admin.register(Plane)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "adding_date")
    list_filter = ("adding_date", )
