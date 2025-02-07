from django.core.management.base import BaseCommand
from workouts.models import Exercise

class Command(BaseCommand):
    help = 'Seed the database with predefined exercises'

    def handle(self, *args, **options):
        exercises = [
            {"name": "Push-up", "description": "Push-ups build upper body strength.",
             "instructions": "Lower yourself on the hands and push up.", "target_muscles": "Chest, Triceps, Shoulders"},
             
            {"name": "Squat", "description": "A strength exercise where you lower your hips from a standing position.",
             "instructions": "Lower your hips, keep your back straight.", "target_muscles": "Legs, Glutes"},
             
            {"name": "Deadlift", "description": "Lift weight from the ground to thigh level using your legs and hips.",
             "instructions": "Lift the barbell while keeping your back straight.", "target_muscles": "Back, Hamstrings"},

            {"name": "Pull-up", "description": "Lift yourself using a horizontal bar.",
             "instructions": "Grip the bar, pull yourself up until your chin is above the bar, then lower down.", "target_muscles": "Back, Biceps"},
             
            {"name": "Bench Press", "description": "A weightlifting exercise pressing a barbell away from your chest.",
             "instructions": "Lie on a bench, grip the barbell, lower it to your chest, then press it up.", "target_muscles": "Chest, Triceps, Shoulders"},
             
            {"name": "Lunges", "description": "A lower-body exercise strengthening the legs and glutes.",
             "instructions": "Step forward, lower your back knee to the ground, then push back up.", "target_muscles": "Legs, Glutes"},
             
            {"name": "Plank", "description": "A core exercise where you hold a push-up position.",
             "instructions": "Keep your body straight, engage your core, and hold.", "target_muscles": "Core, Shoulders"},
             
            {"name": "Dumbbell Shoulder Press", "description": "An overhead pressing movement using dumbbells.",
             "instructions": "Press the dumbbells overhead, then lower slowly.", "target_muscles": "Shoulders, Triceps"},
             
            {"name": "Bicep Curl", "description": "A movement isolating the biceps.",
             "instructions": "Curl the dumbbells towards your shoulders, then lower down.", "target_muscles": "Biceps"},
             
            {"name": "Tricep Dips", "description": "Strengthens the triceps using parallel bars or a bench.",
             "instructions": "Lower yourself down until your arms are at 90 degrees, then press up.", "target_muscles": "Triceps, Shoulders"},
             
            {"name": "Leg Press", "description": "A machine-based exercise for the lower body.",
             "instructions": "Push the platform away using your legs, then lower it slowly.", "target_muscles": "Legs, Glutes"},
             
            {"name": "Calf Raises", "description": "Strengthens the calf muscles.",
             "instructions": "Stand on your toes, raise your heels, then lower back down.", "target_muscles": "Calves"},
             
            {"name": "Lat Pulldown", "description": "Targets the upper back using a machine.",
             "instructions": "Pull the bar down towards your chest, then release it slowly.", "target_muscles": "Back, Biceps"},
             
            {"name": "Burpees", "description": "A full-body conditioning exercise.",
             "instructions": "Drop into a squat, kick your legs back, do a push-up, jump back up.", "target_muscles": "Full Body"},
             
            {"name": "Mountain Climbers", "description": "A cardio and core exercise in a plank position.",
             "instructions": "Run your knees towards your chest alternately at a fast pace.", "target_muscles": "Core, Shoulders, Legs"},
             
            {"name": "Box Jumps", "description": "A plyometric exercise building explosive power.",
             "instructions": "Jump onto a sturdy box or platform, then step down and repeat.", "target_muscles": "Legs, Glutes"},
             
            {"name": "Farmer's Walk", "description": "A strength and endurance exercise carrying weights while walking.",
             "instructions": "Hold a heavy dumbbell in each hand, keep your posture straight, and walk forward.", "target_muscles": "Grip Strength, Core, Shoulders, Legs"},
             
            {"name": "Hanging Leg Raises", "description": "An advanced core exercise hanging from a bar.",
             "instructions": "Hang from a bar, keep your legs straight, and lift them towards your chest, then lower slowly.", "target_muscles": "Core, Hip Flexors"},

            {"name": "Jump Rope", "description": "A cardio exercise improving coordination and endurance.",
             "instructions": "Jump over the rope continuously while keeping a steady rhythm.", "target_muscles": "Legs, Calves, Cardio"},
             
            {"name": "Face Pulls", "description": "A cable exercise improving shoulder and upper back stability.",
             "instructions": "Pull the cable towards your face, keeping elbows high.", "target_muscles": "Shoulders, Upper Back"},
             
            {"name": "Hip Thrusts", "description": "A glute activation exercise using a barbell or bodyweight.",
             "instructions": "Push your hips up while keeping your shoulders on a bench.", "target_muscles": "Glutes, Hamstrings"},
             
            {"name": "Rowing Machine", "description": "A full-body cardio and strength exercise.",
             "instructions": "Pull the handle while pushing with your legs, then return to start.", "target_muscles": "Back, Legs, Cardio"},
        ]

        for exercise_data in exercises:
            Exercise.objects.update_or_create(
                name=exercise_data["name"],
                defaults=exercise_data
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded 22 exercises."))
