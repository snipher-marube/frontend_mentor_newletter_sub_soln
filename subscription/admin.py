from django.contrib import admin

from .models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    list_filter = ('date',)
    search_fields = ('email',)
    date_hierarchy = 'date'
    ordering = ('-date',)
    readonly_fields = ('date',)
    fieldsets = (
        (None, {
            'fields': ('email', 'date')
        }),
    )
    
