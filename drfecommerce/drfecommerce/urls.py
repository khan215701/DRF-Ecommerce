from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drfecommerce.product import views
router = DefaultRouter()
router.register(r"category",views.CategoryView, basename="category-list")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("api/", include(router.urls))
]
