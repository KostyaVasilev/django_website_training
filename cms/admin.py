from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider


class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    list_display_links = ('cms_title',)  # кортеж, запятая обяз.
    list_editable = ('cms_css',)  # кортеж, запятая обяз.
    fields = ('cms_title', 'cms_text', 'cms_css', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.cms_img:
            return mark_safe(f'<img src="{obj.cms_img.url}" width="80px"')
        else:
            return 'Нет картинки.'

    get_img.short_description = 'Миниатюра'

# Register your models here.
admin.site.register(CmsSlider, CmsAdmin)

