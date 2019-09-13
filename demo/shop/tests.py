from django.test import TestCase
from shop.models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        self.name = 'green-bag'
        self.slug = 'green_bag'
        Category.objects.create(name=self.name, slug=self.slug)

    def test_get_category(self):
        green_bag = Category.objects.get(name=self.name)
        self.assertEqual(green_bag.slug, self.slug)
        print('test_get_category')
