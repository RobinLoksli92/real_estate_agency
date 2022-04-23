from django.contrib import admin
from .models import Flat, Dislike


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner','town','address', 'owner_pure_phone')
    readonly_fields = ["created_at"]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owner_pure_phone', 'owners_phonenumber')
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']

class DislikeAdmin(admin.ModelAdmin):
    raw_id_fields = ['disliked_flat']

admin.site.register(Flat, FlatAdmin)
admin.site.register(Dislike, DislikeAdmin)
