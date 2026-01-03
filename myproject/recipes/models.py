from django.db import models

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Snacks', 'Snacks'),
        ('Drinks', 'Drinks'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Lunch')
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title
