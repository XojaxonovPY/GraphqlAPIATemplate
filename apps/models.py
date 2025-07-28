from django.db.models import Model, CharField, DecimalField, ForeignKey, CASCADE, FileField, TextChoices


class Category(Model):
    name=CharField(max_length=100)

class Product(Model):
    class ProductStatus(TextChoices):
        NEW = 'new','New'
        OLD = 'old','Old'
    name=CharField(max_length=100)
    price=DecimalField(max_digits=10,decimal_places=2)
    category=ForeignKey('apps.Category',related_name='products',on_delete=CASCADE)
    image=FileField(upload_to='images/',null=True,blank=True)
    status=CharField(max_length=100,choices=ProductStatus.choices,default=ProductStatus.NEW)





