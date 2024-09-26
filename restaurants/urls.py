from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, MenuViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = router.urls
