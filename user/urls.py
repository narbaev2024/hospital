from django.urls import path
from .views import UserProfileViewSet, DoctorViewSet,  MedicationViewSet, FitnessProgramViewSet


urlpatterns = [

    path('', DoctorViewSet.as_view({'get': 'list', 'post': 'create'}), name='doctor_list'),
    path('<int:pk>/', DoctorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='doctor_detail'),
    path('', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile_list'),
    path('<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='userprofile_detail'),
    path('', MedicationViewSet.as_view({'get': 'list', 'post': 'create'}), name='name_list'),
    path('<int:pk>/', MedicationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='name_detail'),
    path('', FitnessProgramViewSet.as_view({'get': 'list', 'post': 'create'}), name='name_list'),
    path('<int:pk>/', FitnessProgramViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='name_detail'),
]