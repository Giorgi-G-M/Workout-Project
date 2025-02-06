from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, WorkoutPlanViewSet, TrackingViewSet


router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'workout-plans', WorkoutPlanViewSet)
router.register(r'tracking', TrackingViewSet)


urlpatterns = [
    path('', include(router.urls))
]