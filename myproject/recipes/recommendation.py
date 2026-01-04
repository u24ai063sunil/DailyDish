from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .models import Recipe


class RecipeRecommender:
    """
    AI-powered recipe recommendation system using content-based filtering.
    Recommends recipes based on ingredients, cuisine, difficulty, and dietary preferences.
    """
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(
            max_features=1000,
            stop_words='english',
            ngram_range=(1, 2)
        )
    
    def create_recipe_features(self, recipe):
        """
        Create a feature string combining all recipe attributes.
        """
        features = []
        
        # Add ingredients (most important)
        if recipe.ingredients:
            features.append(recipe.ingredients.lower())
        
        # Add cuisine (weighted by repeating)
        if recipe.cuisine:
            features.append(f"{recipe.cuisine.lower()} " * 3)
        
        # Add category
        features.append(f"{recipe.category.lower()} " * 2)
        
        # Add difficulty
        features.append(recipe.difficulty.lower())
        
        # Add dietary preferences
        if recipe.is_vegan:
            features.append("vegan plant-based " * 2)
        elif recipe.is_vegetarian:
            features.append("vegetarian meatless " * 2)
        
        # Add description
        if recipe.description:
            features.append(recipe.description.lower())
        
        return ' '.join(features)
    
    def get_recommendations(self, recipe_id, num_recommendations=6, user=None):
        """
        Get recipe recommendations based on a given recipe.
        
        Args:
            recipe_id: ID of the recipe to base recommendations on
            num_recommendations: Number of recommendations to return
            user: Current user (to exclude their own recipes if needed)
        
        Returns:
            List of recommended Recipe objects
        """
        try:
            # Get the base recipe
            base_recipe = Recipe.objects.get(id=recipe_id)
            
            # Get all recipes except the base recipe
            all_recipes = Recipe.objects.exclude(id=recipe_id)
            
            # Optionally exclude user's own recipes from recommendations
            if user and user.is_authenticated:
                # Include user's recipes but with lower priority
                pass
            
            if not all_recipes.exists():
                return []
            
            # Create feature strings for all recipes
            recipe_list = [base_recipe] + list(all_recipes)
            feature_strings = [self.create_recipe_features(recipe) for recipe in recipe_list]
            
            # Create TF-IDF matrix
            tfidf_matrix = self.vectorizer.fit_transform(feature_strings)
            
            # Calculate cosine similarity between base recipe and all others
            cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
            
            # Get indices of top similar recipes
            similar_indices = cosine_similarities.argsort()[-num_recommendations:][::-1]
            
            # Get the recommended recipes
            recommended_recipes = [list(all_recipes)[i] for i in similar_indices]
            
            return recommended_recipes
            
        except Recipe.DoesNotExist:
            return []
        except Exception as e:
            print(f"Recommendation error: {e}")
            return []
    
    def get_personalized_recommendations(self, user, num_recommendations=6):
        """
        Get personalized recommendations based on user's recipe history.
        
        Args:
            user: User object
            num_recommendations: Number of recommendations to return
        
        Returns:
            List of recommended Recipe objects
        """
        if not user.is_authenticated:
            # Return popular recipes for non-authenticated users
            return Recipe.objects.all().order_by('-created_at')[:num_recommendations]
        
        # Get user's recipes
        user_recipes = Recipe.objects.filter(author=user)
        
        if not user_recipes.exists():
            # New user - return popular or recent recipes
            return Recipe.objects.exclude(author=user).order_by('-created_at')[:num_recommendations]
        
        # Analyze user's preferences
        user_cuisines = user_recipes.values_list('cuisine', flat=True).distinct()
        user_categories = user_recipes.values_list('category', flat=True).distinct()
        is_vegetarian = user_recipes.filter(is_vegetarian=True).exists()
        is_vegan = user_recipes.filter(is_vegan=True).exists()
        
        # Get recipes from other users
        candidate_recipes = Recipe.objects.exclude(author=user)
        
        # Score recipes based on user preferences
        scored_recipes = []
        
        for recipe in candidate_recipes[:100]:  # Limit for performance
            score = 0
            
            # Cuisine match
            if recipe.cuisine in user_cuisines:
                score += 3
            
            # Category match
            if recipe.category in user_categories:
                score += 2
            
            # Dietary preference match
            if is_vegan and recipe.is_vegan:
                score += 3
            elif is_vegetarian and recipe.is_vegetarian:
                score += 2
            
            # Difficulty preference (assume users like similar difficulty)
            user_avg_difficulty = {'Easy': 1, 'Medium': 2, 'Hard': 3}
            user_difficulties = [user_avg_difficulty.get(r.difficulty, 2) for r in user_recipes]
            avg_user_difficulty = sum(user_difficulties) / len(user_difficulties) if user_difficulties else 2
            recipe_difficulty = user_avg_difficulty.get(recipe.difficulty, 2)
            
            if abs(avg_user_difficulty - recipe_difficulty) <= 1:
                score += 1
            
            scored_recipes.append((recipe, score))
        
        # Sort by score and return top recommendations
        scored_recipes.sort(key=lambda x: x[1], reverse=True)
        recommendations = [recipe for recipe, score in scored_recipes[:num_recommendations]]
        
        # If not enough recommendations, fill with recent recipes
        if len(recommendations) < num_recommendations:
            additional = Recipe.objects.exclude(author=user).exclude(
                id__in=[r.id for r in recommendations]
            ).order_by('-created_at')[:num_recommendations - len(recommendations)]
            recommendations.extend(additional)
        
        return recommendations
    
    def get_similar_by_ingredients(self, ingredients_text, num_recommendations=6):
        """
        Find recipes with similar ingredients.
        
        Args:
            ingredients_text: String of ingredients to match
            num_recommendations: Number of recommendations to return
        
        Returns:
            List of recommended Recipe objects
        """
        all_recipes = Recipe.objects.all()
        
        if not all_recipes.exists():
            return []
        
        # Create feature strings
        feature_strings = [ingredients_text.lower()] + [
            self.create_recipe_features(recipe) for recipe in all_recipes
        ]
        
        # Create TF-IDF matrix
        tfidf_matrix = self.vectorizer.fit_transform(feature_strings)
        
        # Calculate similarity
        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
        
        # Get top matches
        top_indices = similarities.argsort()[-num_recommendations:][::-1]
        
        recommended_recipes = [list(all_recipes)[i] for i in top_indices]
        
        return recommended_recipes