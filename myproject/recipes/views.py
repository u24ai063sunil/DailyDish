from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Recipe, UserProfile
from .forms import RegisterForm, LoginForm, UserProfileForm, UserUpdateForm


# Authentication Views
def register_view(request):
    if request.user.is_authenticated:
        return redirect('recipe_list')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile
            UserProfile.objects.create(user=user)
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    
    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('recipe_list')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Only show welcome message after successful login
                messages.success(request, f'Welcome back, {username}!')
                return redirect('recipe_list')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    # Don't pass any messages to the template for GET requests
    return render(request, 'auth/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    # Don't show logout message, just redirect
    return redirect('login')


@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_recipes = Recipe.objects.filter(author=request.user)
    
    context = {
        'profile': profile,
        'user_recipes': user_recipes,
        'recipe_count': user_recipes.count(),
    }
    return render(request, 'auth/profile.html', context)


@login_required
def edit_profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'auth/edit_profile.html', context)


# Recipe Views
@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    
    # Only allow deletion if user is admin or recipe author
    if request.user.is_staff or recipe.author == request.user:
        recipe.delete()
        messages.success(request, 'Recipe deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this recipe.')
    
    return redirect('recipe_list')


def popular_recipes(request):
    # Get all recipes except those created by the current user
    if request.user.is_authenticated:
        recipes = Recipe.objects.exclude(author=request.user)[:6]
    else:
        # For non-authenticated users, show latest 6 recipes
        recipes = Recipe.objects.all()[:6]
    return render(request, 'popular_recipes.html', {'recipes': recipes})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        difficulty = request.POST.get('difficulty', 'Medium')
        prep_time = request.POST.get('prep_time')
        cook_time = request.POST.get('cook_time')
        servings = request.POST.get('servings', 4)
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        description = request.POST.get('description', '')
        cuisine = request.POST.get('cuisine', '')
        is_vegetarian = request.POST.get('is_vegetarian') == 'on'
        is_vegan = request.POST.get('is_vegan') == 'on'
        
        Recipe.objects.create(
            title=title,
            category=category,
            difficulty=difficulty,
            prep_time=prep_time,
            cook_time=cook_time,
            servings=servings,
            ingredients=ingredients,
            instructions=instructions,
            description=description,
            cuisine=cuisine,
            is_vegetarian=is_vegetarian,
            is_vegan=is_vegan,
            author=request.user
        )
        messages.success(request, 'Recipe added successfully!')
        return redirect('recipe_list')
    
    return render(request, 'add_recipe.html')


def recipe_list(request):
    recipes = Recipe.objects.all()
    
    # Get filter parameters
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    difficulty_filter = request.GET.get('difficulty', '')
    cuisine_filter = request.GET.get('cuisine', '')
    diet_filter = request.GET.get('diet', '')
    
    # Apply filters
    if search_query:
        recipes = recipes.filter(
            Q(title__icontains=search_query) |
            Q(ingredients__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    if category_filter:
        recipes = recipes.filter(category=category_filter)
    
    if difficulty_filter:
        recipes = recipes.filter(difficulty=difficulty_filter)
    
    if cuisine_filter:
        recipes = recipes.filter(cuisine__icontains=cuisine_filter)
    
    if diet_filter == 'vegetarian':
        recipes = recipes.filter(is_vegetarian=True)
    elif diet_filter == 'vegan':
        recipes = recipes.filter(is_vegan=True)
    
    # Get unique cuisines for filter dropdown
    cuisines = Recipe.objects.exclude(cuisine__isnull=True).exclude(cuisine='').values_list('cuisine', flat=True).distinct()
    
    context = {
        'recipes': recipes,
        'cuisines': cuisines,
        'search_query': search_query,
        'category_filter': category_filter,
        'difficulty_filter': difficulty_filter,
        'cuisine_filter': cuisine_filter,
        'diet_filter': diet_filter,
    }
    
    return render(request, 'recipe_list.html', context)


def recipes_by_category(request, category):
    recipes = Recipe.objects.filter(category=category)
    
    # Get filter parameters
    difficulty_filter = request.GET.get('difficulty', '')
    diet_filter = request.GET.get('diet', '')
    
    # Apply additional filters
    if difficulty_filter:
        recipes = recipes.filter(difficulty=difficulty_filter)
    
    if diet_filter == 'vegetarian':
        recipes = recipes.filter(is_vegetarian=True)
    elif diet_filter == 'vegan':
        recipes = recipes.filter(is_vegan=True)
    
    context = {
        'recipes': recipes,
        'category': category,
        'difficulty_filter': difficulty_filter,
        'diet_filter': diet_filter,
    }
    
    return render(request, 'recipes_by_category.html', context)


# About Page
def about_view(request):
    return render(request, 'about.html')