from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('public/user', views.PublicUserViewSet,
                base_name="public-user")
router.register('user', views.UserViewSet,
                base_name="user")

urlpatterns = router.urls
