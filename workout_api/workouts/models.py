from django.db import models
from django.contrib.auth.models import User



class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(help_text="detailed description of the exercise.")
    instructions = models.TextField(help_text="Instruction for proper excution.")
    target_muscles = models.CharField(max_length=200, help_text="target muscles")

    def __str__(self):
        return self.name
    
class WorkoutPlan(models.Model):
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name="Workout_plan",
        help_text="the user who created workoout plan"
    )
    title = models.CharField(max_length=100, help_text="Name of the workout plan")
    session_duration = models.DurationField(help_text="planned for each workout session (HH:MM:SS)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.user.username}"
    
class WorkoutPlanExercise(models.Model):
    wokrout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE,related_name="exercises")
    exsercies = models.ForeignKey(Exercise,on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField(null=True,blank=True,help_text="number of sets, if applicable")
    distance = models.FloatField(null=True,blank=True, help_text="distance if applicable for running")
    duration = models.DurationField(null=True,blank=True,help_text="duration for exercise if applicabe")
    sets = models.PositiveIntegerField(null=True,blank=True,help_text="number of sets applicable")

    def __str__(self):
        return f"{self.wokrout_plan.title} {self.exsercies.name}"


class tracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tracking")

    weight = models.FloatField(help_text="recorded wieght of the user")
    date = models.DateField(auto_now_add=True)
    note = models.TextField(null=True,blank=True,help_text="optional note for this tracking entry.")

    def __str__(self):
        return f"{self.user.username} {self.weight} on {self.date}"
