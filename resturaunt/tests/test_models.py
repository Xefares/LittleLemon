from django.test import TestCase
from resturaunt.models import MenuItem 

class MenuItemTest(TestCase):
    def test_get_itmem(self):
        item = MenuItem.objects.create(title='IceCream',price = 80, inventory = 100)
        self.assertEqual(str(item), "IceCream : 80")