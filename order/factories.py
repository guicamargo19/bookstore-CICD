# type: ignore
import factory

from django.contrib.auth.models import User
# from product.factories import ProductFactory

from order.models import Order


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for products in extracted:
                self.product.add(products)

    class Meta:
        model = Order
