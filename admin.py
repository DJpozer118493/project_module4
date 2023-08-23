from django.contrib import admin
from .models import Advertisement
from django.db.models.query import QuerySet
# Register your models here.


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'price', 'auction', 'created_at', 
                    'created_date', 'update_date', 'image_display']
    list_filter = ['auction', 'created_at', 'price']
    actions = ['make_action_as_false', 'make_action_as_true']
    fieldsets = (
        ('Общие', {
            "fields": (
                'title', 'description', 'user', 'image'
            ),
        }),
        ('Финансы', {
            "fields": (
                'price', 'auction'
            ),
            'classes': ['collapse']
        })
    )



    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False)
    

    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True)





admin.site.register(Advertisement, AdvertisementAdmin)












