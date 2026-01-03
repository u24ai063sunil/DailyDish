from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_recipe, name='add_recipe'),
    path('', views.recipe_list, name='recipe_list'),
    path('category/<str:category>/', views.recipes_by_category, name='recipes_by_category'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('popular/', views.popular_recipes, name='popular_recipes'),

]
