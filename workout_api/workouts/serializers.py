from rest_framework import serializers
from .models import Exercise, WorkoutPlan, Tracking, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'



class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)


    class Meta:
        model = WorkoutPlan
        fields = '__all__'
        # ('id','user','title','frequency','goal','session_duration','created_at','exercises')
        read_only_fields = ('user','created_at')

class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = '__all__'
        read_only_fields = ('user','date')
