import factory
from drfecommerce.product.models import Category, Brand, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    name = "test_category"
    
class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand
    
    name = "brand_factory"
    
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        
    name = "product_factory"
    description = "check"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)