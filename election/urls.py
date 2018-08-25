from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('candidate', views.CandidateView)

urlpatterns = [
    path('', include(router.urls))
]