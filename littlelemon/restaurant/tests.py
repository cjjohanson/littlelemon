from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

# Create your tests here.
class MenuTest(TestCase):
    def test_get_item(self):
        menu_item = Menu
        item = Menu.objects.create(
            title="Ice Cream",
            price=80,
            inventory=100
        )
        self.assertEqual(str(item), "Ice Cream : 80")


class MenuViewTest(TestCase):
    def setUp(self):
        self.pizza = Menu.objects.create(title='Pizza', price=10.99, inventory=101)
        self.pasta = Menu.objects.create(title='Pasta', price=8.99, inventory=201)

    def test_getall(self):
        menu_items = Menu.objects.all()

        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(serializer.data, [
        {'id': self.pizza.id, 'title': 'Pizza', 'price': '10.99', 'inventory': 101},
        {'id': self.pasta.id, 'title': 'Pasta', 'price': '8.99', 'inventory': 201}
        ])