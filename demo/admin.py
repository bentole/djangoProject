from django.contrib import admin
from django.utils import html
from demo.models import Equipment, Location, Link, Serialnumber
from django.db.models import Q
import time

def update_system_data():
    return 'hi'

# Register your models here.

class UtilFuncs:
    @staticmethod
    def ztp_status(obj, status):
        retvals = {
            'inprogress': 'yellow.png',
            'Provisioned': 'green.png',
            'unknown': 'grey.png',
            'failed': 'red.png'
        }
        retval = retvals.get(status)
        return html.format_html('<img src="/static/{}" width="20", height="20"'.format(retval))
    @staticmethod
    def do_this(obj):
        pass

class LinkInlineFrom(admin.TabularInline):
    fk_name = 'from_location'
    extra = 0
    model = Link
    verbose_name_plural = 'Koblinger til lokasjon'

class LinkInlineTo(admin.TabularInline):
    fk_name = 'to_location'
    extra = 0
    model = Link
    max_num = 0
    readonly_fields = ('from_location', 'sambandsnr' )
    verbose_name_plural = 'Koblinger fra lokasjon'


class EquipmentInline(admin.TabularInline):
    readonly_fields = ('location', 'location_type', 'function', 'model', 'count', 'ztp_status','button')
    extra = 0
    model = Equipment
    verbose_name_plural = 'Utstyrsliste'

    def ztp_status(self, obj):
        status = 'failed'
        return UtilFuncs.ztp_status(obj, status)

    def button(self, obj):
        return html.format_html('<button class="btn btn-primary" type="button" onclick=alert("hei");>test</button>')

class LocationAdmin(admin.ModelAdmin):
    search_fields = ('name','delivery_place')
    list_display = ('name','delivery_place')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    actions = [update_system_data]
    inlines = [
        EquipmentInline,
        LinkInlineFrom,
        LinkInlineTo,
    ]

class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ('location__name','function')
    list_display = ('function', 'location', 'model', 'serial_number')
    readonly_fields = ('location', 'location_type', 'function', 'model', 'count')

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if not isinstance(inline, LinkInlineFrom) or obj is not None:
                inline
                yield inline.get_formset(request, obj), inline

class LinkAdmin(admin.ModelAdmin):
    pass
    #readonly_fields = ('side_a_intf', 'side_b_intf', 'ip_address')

class SerialnumberAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Serialnumber, SerialnumberAdmin)
