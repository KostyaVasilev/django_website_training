from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)  # Кортеж,запятая после един. знач. обяз.
    extra = 1  # Кол-во полей кооментария, по дефолту три.




class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone',
                    'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_status', 'order_name',
                    'order_dt')
    list_filter = ('order_status', 'order_dt',)
    list_editable = ('order_status', 'order_phone')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')
    inlines = (Comment,)  # Кортеж, запятая после единственного значения обяз.



# Register your models here.
admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)