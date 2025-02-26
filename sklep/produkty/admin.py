from django.contrib import admin
from .models import Produkt
from django.utils.html import format_html

class ProduktAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'cena', 'link_do_strony')

    def link_do_strony(self, obj):
        return format_html('<a href="{}">Zobacz na stronie</a>', f'/{obj.id}/')

    link_do_strony.short_description = 'Link do strony produktu'

admin.site.register(Produkt, ProduktAdmin)
