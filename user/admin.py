from django.contrib import admin
from user.models import User, Post, PostComment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = [
        "Name",
        "Phone",
    ]
    search_fields = ("Phone", "Name")
    ordering = ("Created",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = [
        "User",
        "Title",
    ]
    search_fields = ["Title", "User__Name"]
    ordering = ("Created",)


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = [
        "Post",
        "User",
    ]
    ordering = ("Created",)
