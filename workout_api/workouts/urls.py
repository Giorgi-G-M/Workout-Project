from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseViewSet, WorkoutPlanViewSet, TrackingViewSet, UserViewSet


router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'workout-plans', WorkoutPlanViewSet)
router.register(r'tracking', TrackingViewSet)
router.register(r'user',UserViewSet)


urlpatterns = [
    path('', include(router.urls))

]