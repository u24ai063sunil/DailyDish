from django.contrib import admin
from .models import Recipe, UserProfile

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'author', 'created_at']
    list_filter = ['category', 'difficulty', 'is_vegetarian', 'is_vegan']
    search_fields = ['title', 'ingredients', 'description']
    
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'favorite_cuisine', 'created_at']
    search_fields = ['user__username', 'location']