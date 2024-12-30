from django.test import TestCase
from resturaunt.models import MenuItem
from resturaunt.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
       MenuItem.objects.create(title='IceCream',price = 80, inventory = 100)
       MenuItem.objects.create(title='Cheesecake',price = 180, inventory = 100)
       MenuItem.objects.create(title='Cake',price = 40, inventory = 100)


    def test_getall(self):
        menu = MenuItem.objects.all()
        serialized_menu = MenuItemSerializer(menu,many=True)
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(serialized_menu.data,response.data)