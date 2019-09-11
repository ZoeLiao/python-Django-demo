from django.test import TestCase
from shop.models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        self.name = 'green-package'
        self.slug = 'green_package'
        Category.objects.create(name=self.name, slug=self.slug)

    def test_get_category(self):
        green_package = Category.objects.get(name=self.name)
        self.assertEqual(green_package.slug, self.slug)
