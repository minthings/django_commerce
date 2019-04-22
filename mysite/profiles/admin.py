from django.contrib import admin
from .models import profiles


class profilesAdmin(admin.ModelAdmin):
    class Meta:
        model = profiles
admin.site.register(profiles, profilesAdmin)
# Register your models here.
