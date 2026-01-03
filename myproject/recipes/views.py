from django.shortcuts import render, redirect
from .models import Recipe

from django.shortcuts import get_object_or_404

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')

def popular_recipes(request):
    # Hardcoded or inbuilt recipe list
    popular = [
        {
            "title": "Matar Paneer",
            "category": "Lunch",
            "ingredients": "Paneer, Green Peas, Tomatoes, Onions, Spices",
            "instructions": "Cook onions and tomatoes with spices, add peas and paneer, simmer till cooked."
        },
        {
            "title": "Daal Dhokli",
            "category": "Dinner",
            "ingredients": "Wheat flour, Tur dal, Spices, Curry leaves, Ghee",
            "instructions": "Prepare dal with spices. Add rolled wheat dough pieces. Boil until soft."
        },
        {
            "title": "Ghewar",
            "category": "Dessert",
            "ingredients": "Flour, Ghee, Sugar syrup, Milk, Cardamom",
            "instructions": "Make ghewar in ghee, soak in sugar syrup, top with rabri or dry fruits."
        },
        {
            "title": "Classic Pancakes",
            "category": "Breakfast",
            "ingredients": "Flour, Milk, Eggs, Sugar, Baking Powder",
            "instructions": "Mix, pour, flip, and serve with syrup."
        },
        {
            "title": "Masala Maggi",
            "category": "Snacks",
            "ingredients": "Maggi, Onion, Tomato, Spices",
            "instructions": "Boil water, add masala and veggies, cook till ready."
        },
        {
            "title": "Cold Coffee",
            "category": "Drinks",
            "ingredients": "Coffee, Milk, Ice, Sugar",
            "instructions": "Blend and serve chilled."
        }
    ]
    return render(request, 'popular_recipes.html', {'recipes': popular})


def add_recipe(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        ingredients = request.POST['ingredients']
        instructions = request.POST['instructions']
        Recipe.objects.create(title=title, category=category, ingredients=ingredients, instructions=instructions)
        return redirect('recipe_list')
    return render(request, 'add_recipe.html')


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipes_by_category(request, category):
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipes_by_category.html', {'recipes': recipes, 'category': category})

