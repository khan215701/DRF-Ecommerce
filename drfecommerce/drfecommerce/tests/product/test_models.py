import pytest
pytestmark =  pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        x = category_factory()
        assert x.__str__() == "test_category"
        
class TestBrandModel:
    def test_str_method(self, brand_factory):
        obj = brand_factory()
        assert obj.__str__() == "brand_factory"
        
class TestProductModel:
    def test_str_method(self, product_factory):
        obj = product_factory()
        assert obj.__str__() == "product_factory"