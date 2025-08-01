from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, DecimalField, FileField, TextChoices, IntegerField, ForeignKey, CASCADE, \
    ImageField


class Product(Model):
    class ProductStatus(TextChoices):
        NEW = 'new','New'
        OLD = 'old','Old'
    name=CharField(max_length=100)
    price=DecimalField(max_digits=10,decimal_places=2)
    quantity=IntegerField(default=0)
    image=CharField(null=True,blank=True)

class User(AbstractUser):
    age=IntegerField()
    phone_number=CharField(max_length=20)
    username = CharField(max_length=120,null=True,blank=True)


class Order(Model):
    user_id=ForeignKey('apps.User',on_delete=CASCADE)
    amount=DecimalField(max_digits=10,decimal_places=2)

class OrderItem(Model):
    order_id=ForeignKey('apps.Order',on_delete=CASCADE)
    product_id=ForeignKey('apps.Product',on_delete=CASCADE)
    quantity=IntegerField()


class Media(Model):
    image=ImageField(upload_to='media/')


