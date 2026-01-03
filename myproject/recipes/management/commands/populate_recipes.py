from django.core.management.base import BaseCommand
from recipes.models import Recipe

class Command(BaseCommand):
    help = 'Populate database with detailed recipes'

    def handle(self, *args, **kwargs):
        # Clear existing recipes
        Recipe.objects.all().delete()
        
        recipes_data = [
            # Breakfast Recipes
            {
                'title': 'Classic Pancakes',
                'category': 'Breakfast',
                'difficulty': 'Easy',
                'prep_time': 10,
                'cook_time': 15,
                'servings': 4,
                'cuisine': 'American',
                'is_vegetarian': True,
                'description': 'Fluffy, golden pancakes perfect for a weekend breakfast.',
                'ingredients': '''2 cups all-purpose flour
2 tablespoons sugar
2 teaspoons baking powder
1/2 teaspoon salt
2 eggs
1 3/4 cups milk
1/4 cup melted butter
1 teaspoon vanilla extract''',
                'instructions': '''1. In a large bowl, whisk together flour, sugar, baking powder, and salt.
2. In another bowl, beat eggs and mix in milk, melted butter, and vanilla.
3. Pour wet ingredients into dry ingredients and stir until just combined (lumps are okay).
4. Heat a griddle or pan over medium heat and lightly grease it.
5. Pour 1/4 cup batter for each pancake.
6. Cook until bubbles form on surface, then flip and cook until golden brown.
7. Serve hot with maple syrup, butter, and fresh berries.'''
            },
            {
                'title': 'Masala Omelette',
                'category': 'Breakfast',
                'difficulty': 'Easy',
                'prep_time': 5,
                'cook_time': 10,
                'servings': 2,
                'cuisine': 'Indian',
                'is_vegetarian': True,
                'description': 'Spicy Indian-style omelette with onions, tomatoes, and green chilies.',
                'ingredients': '''4 eggs
1 small onion, finely chopped
1 small tomato, finely chopped
2 green chilies, chopped
2 tablespoons coriander leaves, chopped
1/4 teaspoon turmeric powder
1/2 teaspoon red chili powder
Salt to taste
2 tablespoons oil''',
                'instructions': '''1. Beat eggs in a bowl with salt, turmeric, and chili powder.
2. Add chopped onions, tomatoes, green chilies, and coriander leaves.
3. Heat oil in a pan over medium heat.
4. Pour the egg mixture and spread evenly.
5. Cook for 2-3 minutes until bottom is set.
6. Flip carefully and cook the other side for 2 minutes.
7. Serve hot with bread or toast.'''
            },
            {
                'title': 'Avocado Toast',
                'category': 'Breakfast',
                'difficulty': 'Easy',
                'prep_time': 5,
                'cook_time': 5,
                'servings': 2,
                'cuisine': 'International',
                'is_vegetarian': True,
                'is_vegan': True,
                'description': 'Trendy and healthy breakfast with creamy avocado on crispy toast.',
                'ingredients': '''2 ripe avocados
4 slices whole grain bread
1 lemon (juice)
2 tablespoons olive oil
Salt and pepper to taste
Red pepper flakes (optional)
Cherry tomatoes (optional)
Microgreens (optional)''',
                'instructions': '''1. Toast the bread slices until golden and crispy.
2. Cut avocados in half, remove pit, and scoop flesh into a bowl.
3. Mash avocados with lemon juice, salt, and pepper.
4. Spread avocado mixture generously on toasted bread.
5. Drizzle with olive oil.
6. Top with red pepper flakes, cherry tomatoes, or microgreens if desired.
7. Serve immediately.'''
            },
            
            # Lunch Recipes
            {
                'title': 'Matar Paneer',
                'category': 'Lunch',
                'difficulty': 'Medium',
                'prep_time': 15,
                'cook_time': 30,
                'servings': 4,
                'cuisine': 'Indian',
                'is_vegetarian': True,
                'description': 'Popular North Indian curry with paneer and green peas in a rich tomato gravy.',
                'ingredients': '''250g paneer, cubed
1 cup green peas (fresh or frozen)
3 tomatoes, pureed
1 large onion, finely chopped
2 tablespoons ginger-garlic paste
2 green chilies, slit
1 teaspoon cumin seeds
1/2 teaspoon turmeric powder
1 teaspoon coriander powder
1 teaspoon garam masala
1/2 teaspoon red chili powder
1/2 cup cream
3 tablespoons oil
Salt to taste
Fresh coriander for garnish''',
                'instructions': '''1. Heat oil in a pan and lightly fry paneer cubes until golden. Set aside.
2. In the same pan, add cumin seeds and let them splutter.
3. Add chopped onions and sauté until golden brown.
4. Add ginger-garlic paste and green chilies, cook for 2 minutes.
5. Add turmeric, coriander powder, and red chili powder. Mix well.
6. Pour in tomato puree and cook for 10 minutes until oil separates.
7. Add green peas and 1 cup water. Cook for 5-7 minutes.
8. Add fried paneer cubes and garam masala.
9. Stir in cream and simmer for 3-4 minutes.
10. Garnish with coriander and serve with naan or rice.'''
            },
            {
                'title': 'Chicken Caesar Salad',
                'category': 'Lunch',
                'difficulty': 'Easy',
                'prep_time': 15,
                'cook_time': 15,
                'servings': 2,
                'cuisine': 'Italian-American',
                'is_vegetarian': False,
                'description': 'Classic Caesar salad with grilled chicken, crispy romaine, and creamy dressing.',
                'ingredients': '''2 chicken breasts
1 large romaine lettuce head
1/2 cup Caesar dressing
1/2 cup grated Parmesan cheese
1 cup croutons
2 tablespoons olive oil
Salt and black pepper
1 teaspoon garlic powder
Lemon wedges for serving''',
                'instructions': '''1. Season chicken breasts with salt, pepper, and garlic powder.
2. Heat olive oil in a grill pan and cook chicken for 6-7 minutes per side.
3. Let chicken rest for 5 minutes, then slice into strips.
4. Wash and chop romaine lettuce into bite-sized pieces.
5. In a large bowl, toss lettuce with Caesar dressing.
6. Add croutons and half of the Parmesan cheese.
7. Top with sliced chicken and remaining Parmesan.
8. Serve immediately with lemon wedges.'''
            },
            {
                'title': 'Vegetable Fried Rice',
                'category': 'Lunch',
                'difficulty': 'Easy',
                'prep_time': 15,
                'cook_time': 15,
                'servings': 4,
                'cuisine': 'Chinese',
                'is_vegetarian': True,
                'is_vegan': True,
                'description': 'Quick and delicious fried rice loaded with colorful vegetables.',
                'ingredients': '''3 cups cooked rice (preferably day-old)
1 cup mixed vegetables (carrots, beans, corn, peas)
1 capsicum, diced
1 onion, chopped
3 cloves garlic, minced
2 tablespoons soy sauce
1 tablespoon vinegar
1 teaspoon chili sauce
2 spring onions, chopped
3 tablespoons oil
Salt and pepper to taste''',
                'instructions': '''1. Heat oil in a large wok or pan over high heat.
2. Add garlic and sauté for 30 seconds until fragrant.
3. Add onions and capsicum, stir-fry for 2 minutes.
4. Add mixed vegetables and cook for 3-4 minutes.
5. Push vegetables to the side and add cooked rice.
6. Break up any clumps and stir-fry for 3-4 minutes.
7. Add soy sauce, vinegar, and chili sauce. Mix well.
8. Season with salt and pepper.
9. Garnish with spring onions and serve hot.'''
            },
            
            # Dinner Recipes
            {
                'title': 'Daal Dhokli',
                'category': 'Dinner',
                'difficulty': 'Medium',
                'prep_time': 20,
                'cook_time': 40,
                'servings': 4,
                'cuisine': 'Gujarati',
                'is_vegetarian': True,
                'description': 'Traditional Gujarati comfort food with wheat dumplings in spiced lentil curry.',
                'ingredients': '''For Dal:
1 cup toor dal (pigeon peas)
3 cups water
1 teaspoon turmeric powder
2 tablespoons peanuts
2 tablespoons jaggery
1 tablespoon tamarind paste
Salt to taste

For Dhokli:
1 cup wheat flour
1/4 teaspoon turmeric powder
1/2 teaspoon red chili powder
1 tablespoon oil
Salt to taste
Water as needed

For Tempering:
2 tablespoons ghee
1 teaspoon mustard seeds
1/2 teaspoon cumin seeds
Pinch of asafoetida
10-12 curry leaves
2 dried red chilies
Fresh coriander for garnish''',
                'instructions': '''1. Pressure cook dal with turmeric and water for 3-4 whistles.
2. For dhokli dough: Mix wheat flour, turmeric, chili powder, salt, oil, and water to make firm dough. Rest for 15 minutes.
3. Roll dough thin and cut into diamond shapes.
4. Add peanuts, jaggery, tamarind, and salt to cooked dal.
5. Bring dal to boil and add dhokli pieces one by one.
6. Cook for 15-20 minutes until dhokli is cooked through, stirring occasionally.
7. For tempering: Heat ghee, add mustard seeds, cumin, asafoetida, curry leaves, and red chilies.
8. Pour tempering over dal dhokli.
9. Garnish with coriander and serve hot.'''
            },
            {
                'title': 'Spaghetti Carbonara',
                'category': 'Dinner',
                'difficulty': 'Medium',
                'prep_time': 10,
                'cook_time': 20,
                'servings': 4,
                'cuisine': 'Italian',
                'is_vegetarian': False,
                'description': 'Creamy Italian pasta with bacon, eggs, and Parmesan cheese.',
                'ingredients': '''400g spaghetti
200g bacon or pancetta, diced
4 egg yolks
1 whole egg
1 cup grated Parmesan cheese
3 cloves garlic, minced
Black pepper, freshly ground
Salt to taste
2 tablespoons olive oil
Fresh parsley for garnish''',
                'instructions': '''1. Cook spaghetti in salted boiling water according to package directions. Reserve 1 cup pasta water.
2. While pasta cooks, fry bacon in olive oil until crispy. Add garlic in last minute.
3. In a bowl, whisk together egg yolks, whole egg, and Parmesan cheese.
4. Drain pasta and add to bacon pan (off heat).
5. Quickly add egg mixture, tossing continuously.
6. Add pasta water gradually to create creamy sauce.
7. Season generously with black pepper.
8. Serve immediately with extra Parmesan and parsley.'''
            },
            {
                'title': 'Grilled Salmon with Vegetables',
                'category': 'Dinner',
                'difficulty': 'Medium',
                'prep_time': 15,
                'cook_time': 20,
                'servings': 2,
                'cuisine': 'International',
                'is_vegetarian': False,
                'description': 'Healthy and delicious grilled salmon with roasted vegetables.',
                'ingredients': '''2 salmon fillets (150g each)
2 cups mixed vegetables (broccoli, bell peppers, zucchini)
3 tablespoons olive oil
2 cloves garlic, minced
1 lemon (juice and zest)
1 teaspoon dried herbs (thyme, rosemary)
Salt and black pepper to taste
Fresh dill for garnish''',
                'instructions': '''1. Preheat oven to 200°C (400°F).
2. Season salmon with salt, pepper, lemon juice, and herbs.
3. Toss vegetables with olive oil, garlic, salt, and pepper.
4. Arrange vegetables on a baking tray.
5. Place salmon fillets on top of vegetables.
6. Roast for 15-18 minutes until salmon is cooked through.
7. Garnish with lemon zest and fresh dill.
8. Serve immediately with rice or quinoa.'''
            },
            
            # Dessert Recipes
            {
                'title': 'Ghewar',
                'category': 'Dessert',
                'difficulty': 'Hard',
                'prep_time': 30,
                'cook_time': 30,
                'servings': 8,
                'cuisine': 'Rajasthani',
                'is_vegetarian': True,
                'description': 'Traditional Rajasthani honeycomb dessert soaked in sugar syrup.',
                'ingredients': '''For Ghewar:
2 cups all-purpose flour
1/2 cup ghee
1/2 cup milk
2 cups ice-cold water
Ghee for deep frying

For Sugar Syrup:
2 cups sugar
1 cup water
1/4 teaspoon cardamom powder

For Topping:
Rabri or condensed milk
Chopped pistachios and almonds
Silver leaf (optional)''',
                'instructions': '''1. Make sugar syrup: Boil sugar and water until one-string consistency. Add cardamom powder.
2. Beat ghee until fluffy and white.
3. Gradually add flour and mix well.
4. Add milk and ice-cold water to make thin batter.
5. Heat ghee in a wide, deep pan with a 4-inch ring mold.
6. Pour batter from height in circular motion into hot ghee.
7. Fry until golden and crispy with honeycomb texture.
8. Remove carefully and immerse in warm sugar syrup for 2-3 minutes.
9. Top with rabri, nuts, and silver leaf.
10. Serve at room temperature.'''
            },
            {
                'title': 'Chocolate Lava Cake',
                'category': 'Dessert',
                'difficulty': 'Medium',
                'prep_time': 15,
                'cook_time': 12,
                'servings': 4,
                'cuisine': 'French',
                'is_vegetarian': True,
                'description': 'Decadent chocolate cake with a molten chocolate center.',
                'ingredients': '''150g dark chocolate
100g butter
2 eggs
2 egg yolks
1/4 cup sugar
2 tablespoons flour
1/2 teaspoon vanilla extract
Pinch of salt
Butter and cocoa powder for ramekins
Vanilla ice cream for serving''',
                'instructions': '''1. Preheat oven to 220°C (425°F).
2. Grease 4 ramekins with butter and dust with cocoa powder.
3. Melt chocolate and butter together in a double boiler.
4. In a bowl, whisk eggs, egg yolks, and sugar until thick and pale.
5. Add vanilla extract and salt.
6. Fold in melted chocolate mixture.
7. Sift in flour and fold gently.
8. Divide batter among ramekins.
9. Bake for 12-14 minutes until edges are set but center jiggles.
10. Let rest for 1 minute, invert onto plates, and serve with ice cream.'''
            },
            {
                'title': 'Gulab Jamun',
                'category': 'Dessert',
                'difficulty': 'Medium',
                'prep_time': 20,
                'cook_time': 30,
                'servings': 15,
                'cuisine': 'Indian',
                'is_vegetarian': True,
                'description': 'Soft, spongy milk solid balls soaked in rose-flavored sugar syrup.',
                'ingredients': '''For Jamuns:
1 cup milk powder
1/4 cup all-purpose flour
1/4 teaspoon baking soda
2 tablespoons ghee
4-5 tablespoons milk
Ghee or oil for deep frying

For Sugar Syrup:
2 cups sugar
2 cups water
4-5 cardamom pods
1/2 teaspoon rose water
Few saffron strands''',
                'instructions': '''1. Make sugar syrup: Boil sugar and water with cardamom for 10 minutes. Add rose water and saffron. Keep warm.
2. Mix milk powder, flour, and baking soda in a bowl.
3. Add ghee and rub until mixture resembles breadcrumbs.
4. Add milk gradually and knead into soft dough.
5. Divide into 15 equal portions and roll into smooth balls.
6. Heat ghee in a pan on low-medium heat.
7. Fry jamuns slowly, turning constantly, until deep golden brown.
8. Drain and immediately add to warm sugar syrup.
9. Let soak for at least 2 hours before serving.
10. Serve warm or at room temperature.'''
            },
            
            # Snacks Recipes
            {
                'title': 'Masala Maggi',
                'category': 'Snacks',
                'difficulty': 'Easy',
                'prep_time': 5,
                'cook_time': 10,
                'servings': 2,
                'cuisine': 'Indian Fusion',
                'is_vegetarian': True,
                'description': 'Quick and tasty Indian-style instant noodles with vegetables and spices.',
                'ingredients': '''2 packets Maggi noodles
1 onion, chopped
1 tomato, chopped
1 capsicum, chopped
2 green chilies, chopped
1/4 teaspoon turmeric powder
1/2 teaspoon chili powder
2 tablespoons butter
Fresh coriander, chopped
Lemon wedges for serving''',
                'instructions': '''1. Heat butter in a pan.
2. Add onions and green chilies, sauté until soft.
3. Add tomatoes, capsicum, turmeric, and chili powder. Cook for 2 minutes.
4. Add 2.5 cups water and bring to boil.
5. Add Maggi noodles and included masala packets.
6. Cook for 2-3 minutes, stirring occasionally.
7. Garnish with coriander.
8. Serve hot with lemon wedges.'''
            },
            {
                'title': 'Samosa',
                'category': 'Snacks',
                'difficulty': 'Hard',
                'prep_time': 40,
                'cook_time': 30,
                'servings': 12,
                'cuisine': 'Indian',
                'is_vegetarian': True,
                'is_vegan': True,
                'description': 'Crispy triangular pastries filled with spiced potato filling.',
                'ingredients': '''For Dough:
2 cups all-purpose flour
4 tablespoons oil
1/2 teaspoon salt
Water as needed

For Filling:
4 potatoes, boiled and mashed
1 cup green peas
1 teaspoon cumin seeds
1 teaspoon ginger, grated
2 green chilies, chopped
1 teaspoon garam masala
1/2 teaspoon amchur (dry mango powder)
1 teaspoon coriander powder
Salt to taste
2 tablespoons oil
Fresh coriander, chopped
Oil for deep frying''',
                'instructions': '''1. Make dough: Mix flour, salt, and oil. Add water to make firm dough. Rest for 30 minutes.
2. For filling: Heat oil, add cumin seeds.
3. Add ginger, green chilies, and peas. Cook for 2 minutes.
4. Add mashed potatoes and all spices. Mix well and cool.
5. Divide dough into 6 balls. Roll each into oval shape.
6. Cut in half to make semi-circles.
7. Form cone shape by sealing one edge with water.
8. Fill with potato mixture, seal the top edge.
9. Heat oil and deep fry samosas on medium heat until golden.
10. Serve hot with chutney.'''
            },
            {
                'title': 'Garlic Bread',
                'category': 'Snacks',
                'difficulty': 'Easy',
                'prep_time': 10,
                'cook_time': 15,
                'servings': 4,
                'cuisine': 'Italian',
                'is_vegetarian': True,
                'description': 'Crispy, buttery bread with garlic and herbs.',
                'ingredients': '''1 French baguette
100g butter, softened
6 cloves garlic, minced
2 tablespoons fresh parsley, chopped
1/2 cup mozzarella cheese, grated
1/4 teaspoon oregano
Salt to taste
Red chili flakes (optional)''',
                'instructions': '''1. Preheat oven to 200°C (400°F).
2. Slice baguette diagonally without cutting all the way through.
3. Mix butter, garlic, parsley, oregano, and salt.
4. Spread garlic butter mixture between slices and on top.
5. Sprinkle with mozzarella cheese.
6. Wrap in foil (leave top open for crispy texture).
7. Bake for 10-12 minutes.
8. For extra crispiness, broil for 2 minutes.
9. Sprinkle with chili flakes if desired.
10. Serve warm.'''
            },
            
            # Drinks Recipes
            {
                'title': 'Cold Coffee',
                'category': 'Drinks',
                'difficulty': 'Easy',
                'prep_time': 5,
                'cook_time': 0,
                'servings': 2,
                'cuisine': 'International',
                'is_vegetarian': True,
                'description': 'Refreshing iced coffee drink perfect for hot days.',
                'ingredients': '''2 tablespoons instant coffee powder
4 tablespoons sugar (adjust to taste)
4 tablespoons hot water
2 cups cold milk
Ice cubes
Whipped cream (optional)
Chocolate syrup (optional)''',
                'instructions': '''1. In a blender, add coffee powder, sugar, and hot water.
2. Blend until sugar dissolves and mixture is frothy.
3. Add cold milk and ice cubes.
4. Blend until smooth and frothy.
5. Pour into tall glasses.
6. Top with whipped cream and chocolate syrup if desired.
7. Serve immediately with a straw.'''
            },
            {
                'title': 'Mango Lassi',
                'category': 'Drinks',
                'difficulty': 'Easy',
                'prep_time': 5,
                'cook_time': 0,
                'servings': 2,
                'cuisine': 'Indian',
                'is_vegetarian': True,
                'description': 'Creamy, sweet yogurt drink with fresh mango.',
                'ingredients': '''1 cup ripe mango, chopped
1 cup yogurt (curd)
1/2 cup milk
3 tablespoons sugar
1/4 teaspoon cardamom powder
Ice cubes
Saffron strands for garnish (optional)''',
                'instructions': '''1. Add mango, yogurt, milk, sugar, and cardamom to blender.
2. Blend until smooth and creamy.
3. Add ice cubes and blend again.
4. Taste and adjust sweetness if needed.
5. Pour into glasses.
6. Garnish with saffron strands or mango pieces.
7. Serve chilled.'''
            },
            {
                'title': 'Masala Chai',
                'category': 'Drinks',
                'difficulty': 'Easy',
                'prep_time': 5,
                'cook_time': 10,
                'servings': 2,
                'cuisine': 'Indian',
                'is_vegetarian': True,
                'description': 'Aromatic spiced Indian tea with milk.',
                'ingredients': '''2 cups water
1 cup milk
2 tablespoons tea leaves (or 2 tea bags)
2 tablespoons sugar
4-5 cardamom pods, crushed
1-inch ginger, crushed
4-5 black peppercorns
2 cloves
1 small cinnamon stick''',
                'instructions': '''1. In a saucepan, add water and all spices.
2. Bring to boil and simmer for 3-4 minutes.
3. Add tea leaves and sugar.
4. Boil for 2 minutes on high heat.
5. Add milk and bring to boil again.
6. Simmer for 2-3 minutes.
7. Strain into cups using a fine mesh strainer.
8. Serve hot with biscuits or snacks.'''
            },
        ]
        
        for recipe_data in recipes_data:
            Recipe.objects.create(**recipe_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully added: {recipe_data["title"]}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(recipes_data)} recipes!'))