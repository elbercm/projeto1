from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_funcion_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func, views.home)

    def test_category_home_view_funcion_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_details_view_funcion_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)
