from django.contrib import admin
from .models import Recipe, UserProfile

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'author', 'has_video', 'created_at']
    list_filter = ['category', 'difficulty', 'is_vegetarian', 'is_vegan']
    search_fields = ['title', 'ingredients', 'description']
    
    def has_video(self, obj):
        return bool(obj.video_url)
    has_video.boolean = True
    has_video.short_description = 'Video'
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'favorite_cuisine', 'created_at']
    search_fields = ['user__username', 'location']