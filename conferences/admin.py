from django.contrib import admin

from .models import Location, Conference, Tag


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')


class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')


class TagAdmin(admin.ModelAdmin):
    list_display = ('word', 'slug')


admin.site.register(Location, LocationAdmin)
admin.site.register(Conference, ConferenceAdmin)
admin.site.register(Tag, TagAdmin)
