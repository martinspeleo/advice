from info.models import *
from django.contrib import admin

class SectionInline(admin.TabularInline):
    model = Section
    extra = 3

class LeafletAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'url_QR', 'long_QR', 'text', 'order')
    inlines = [SectionInline]

class ItemInline(admin.StackedInline):
    model = Item
    extra = 3

class SectionAdmin(admin.ModelAdmin):
    list_display = ('leaflet', 'title', 'unique', 'required', 'order') 
    inlines = [ItemInline]
    ordering = ('leaflet', 'order')    

admin.site.register(Leaflet, LeafletAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Custom)
