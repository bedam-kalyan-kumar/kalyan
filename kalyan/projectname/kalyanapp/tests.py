# tests.py
from django.test import TestCase
from .models import MyModel

class MyModelTest(TestCase):
    def setUp(self):
        MyModel.objects.create(name="Test Item", description="This is a test description.")

    def test_model_content(self):
        item = MyModel.objects.get(name="Test Item")
        self.assertEqual(item.description, "This is a test description.")
