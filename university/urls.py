from .views import CampusListCreateView, CampusDetailView
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UniversityViewSet
from .views import CourseViewSet

router = DefaultRouter()
router.register('universities', UniversityViewSet)
router.register(r'courses', CourseViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('campus/', CampusListCreateView.as_view(), name='campus-list'),
    path('campus/<int:pk>/', CampusDetailView.as_view(), name='campus-detail'),
]
