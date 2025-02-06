from rest_framework import serializers
from .models import Exercise, WorkoutPlan, WorkoutPlanExercise, tracking


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'



class WorkoutPlanExerciseSerializer(serializers.ModelSerializer):
    execise = ExerciseSerializer(read_only=True)
    execise_id = serializers.PrimaryKeyRelatedField(queryset=Exercise.objects.all(),source='exercise',write_only=True)

    class Meta:
        model = WorkoutPlanExercise
        fields = ('id','exercise','exercise_id','repetitions','sets','duration','distance')


class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = WorkoutPlanExerciseSerializer(may=True, read_only=True)


    class Meta:
        models = WorkoutPlan
        fields = ('id','user','title','frequency','goal','session_duration','created_at','exercises')
        read_only_fields = ('user','created_at')

class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = tracking
        fields = '__all__'
        read_only_fields = ('user','date')
