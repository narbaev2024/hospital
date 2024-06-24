from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import UserProfile, Doctor, MedicalRecord, Appointment, Medication, FitnessProgram, Notification
from .serializers import (
    UserProfileSerializer, DoctorSerializer, MedicalRecordSerializer, AppointmentSerializer,
    MedicationSerializer, FitnessProgramSerializer, NotificationSerializer
)
from .filters import DoctorFilter

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = DoctorFilter
    search_fields = ['license_number']
    permission_classes = [permissions.IsAuthenticated]

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = Appointment


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer


class FitnessProgramViewSet(viewsets.ModelViewSet):
    queryset = FitnessProgram.objects.all()
    serializer_class = FitnessProgramSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

