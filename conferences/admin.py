from django.contrib import admin
from import_export.admin import ImportExportMixin


from .models import Country, Location, Conference, Tag


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class LocationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')


class ConferenceAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    search_fields = ['name', ]


class TagAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('word', 'slug')


admin.site.register(Country, CountryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Tag, TagAdmin)
