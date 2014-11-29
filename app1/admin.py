from django.contrib import admin
from app1.models import Post

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    radio_fields = {'type': admin.VERTICAL}
    list_display = ('pub_date', 'slug', 'title', 'type')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
