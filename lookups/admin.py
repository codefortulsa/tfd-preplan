from django.contrib import admin

from .models import Address, Parcel


class ParcelInlineAdmin(admin.options.InlineModelAdmin):
    model = Parcel
    fields = ('number',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = ('number', 'direction', 'name', 'suffix', 'last_synced',)
    readonly_fields = ('last_synced',)
    
    # FIX: errors with template load issue
    # inlines = (ParcelInlineAdmin,)


@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    fields = ('number', 'address',)
    raw_id_fields = ('address',)
