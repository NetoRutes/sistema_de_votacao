from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('candidate', views.CandidateView)
router.register('election', views.ElectionView)
router.register('vote', views.VoteView)

urlpatterns = [
    path('', include(router.urls))
]