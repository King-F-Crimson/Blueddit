from .models import Post, Community, Profile

from django.contrib import admin

# Register your models here.
class CommunityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)
admin.site.register(Community, CommunityAdmin)
admin.site.register(Profile)