from django.contrib import admin
from .models import Exercise, WorkoutPlan, WorkoutPlanExercise, tracking



admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(WorkoutPlanExercise)
admin.site.register(tracking)
