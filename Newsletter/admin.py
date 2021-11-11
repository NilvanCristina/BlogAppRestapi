from django.contrib import admin
from .models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'date')


admin.site.register(Newsletter, NewsletterAdmin)
