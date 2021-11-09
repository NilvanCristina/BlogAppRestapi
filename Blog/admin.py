from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_status', 'created_on')


admin.site.register(Post, PostAdmin)

admin.site.site_header = "Blog Control Panel"
