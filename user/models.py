from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return
class Doctor(models.Model):
    user = models.CharField(max_length=32, unique=True)
    specialty = models.TextField( )
    license_number = models.CharField(max_length=18, unique=True)
    years_of_experience = models.PositiveIntegerField()
    EDUCATION_CHOISSES = (
        ("Высший", "Высший"),
        ("Средний","Средний")
    )
    education = models.CharField(verbose_name="Диплом", max_length=32, choices=EDUCATION_CHOISSES)
    hospital = models.CharField(max_length=100)

    def __str__(self):
        return self.hospital

class MedicalRecord(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    record_type = models.CharField(max_length=32)
    description = models.TextField()
    date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)



class Appointment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()



class Medication(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)


class FitnessProgram(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    exercises = models.TextField()


class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField()

