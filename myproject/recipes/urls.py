from django.urls import path
from . import views

urlpatterns = [
    # Auth URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    
    # Recipe URLs
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('', views.recipe_list, name='recipe_list'),
    path('category/<str:category>/', views.recipes_by_category, name='recipes_by_category'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('popular/', views.popular_recipes, name='popular_recipes'),
    
    # Static Pages
    path('about/', views.about_view, name='about'),
    path('recommendations/', views.recommendations_view, name='recommendations'),
]