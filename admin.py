from django.contrib import admin

# Register your models here.
from .models import Post, PostDetail


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["title", "content"]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Post
admin.site.register(Post, PostModelAdmin)


class PostDetailAdmin(admin.ModelAdmin):
    list_display = ["category"]
    prepopulated_fields = {'slug': ('category',)}

    class Meta:
        model = PostDetail

admin.site.register(PostDetail, PostDetailAdmin)
