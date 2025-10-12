from django.test import TestCase
from .models import Category, MenuItem

# Create your tests here.

class CategoryModelTest(TestCase):
    def test_str(self):
        cat = Category.objects.create(name="Boissons")
        self.assertEqual(str(cat), "Boissons")

class MenuItemModelTest(TestCase):
    def test_str(self):
        cat = Category.objects.create(name="Pâtisseries")
        item = MenuItem.objects.create(name="Éclair au chocolat", description="Délicieux éclair maison", price=2.50, category=cat)
        self.assertEqual(str(item), "Éclair au chocolat")
    def test_price_decimal(self):
        cat = Category.objects.create(name="Café")
        item = MenuItem.objects.create(name="Espresso", description="Petit café serré", price=1.80, category=cat)
        self.assertEqual(item.price, 1.80)
