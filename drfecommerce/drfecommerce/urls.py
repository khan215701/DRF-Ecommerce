from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drfecommerce.product import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
router = DefaultRouter()
router.register(r"category",views.CategoryView, basename="category-list")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("api/", include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/doc/', SpectacularSwaggerView.as_view(), name="schema_doc"),
]
