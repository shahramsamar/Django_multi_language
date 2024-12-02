from django.contrib import admin

from website.models import  Post    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title','content',)
    list_display = ('title','slug','author','status')
    list_display_links = ('slug','title',)
    list_editable =('status',)
    list_filter = ('slug','status','publish','author')
    prepopulated_fields = {'slug': ('title',)}
    authcomplete_fields =('author',)
    date_hierarchy = 'created'
    ordering = ('-publish', 'status')