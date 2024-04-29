
from django.contrib import admin
from django.urls import path
from appdata.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('donor_register/', donor_register),
    path('doctor_register/', doctor_register),
    path('doctor_login/', doctor_login),
    path('donor_list/', donor_list),
    path('admin_login/', admin_login),
    path('donor_login/', donor_login),
    path('doctor_list/', doctor_list),
    path('doctor_delete/<int:id>', doctor_delete),
    path('patient_request/', patient_request),
    path('admin_patient_request_list/', admin_patient_request_list),
    path('donate_donor_list/<int:id>', donate_donor_list),
    path('donate/<int:id>', donate),
    path('admin_patient_donated_list/', admin_patient_donated_list),
    path('admin_donor_donated_list/', admin_donor_donated_list),
    path('admin_donor_available_list/', admin_donor_available_list),
    path('donor_death/', donor_death),
    path('doctor_patient_request_list/', doctor_patient_request_list),
    path('doctor_donated_patient_list/', doctor_donated_patient_list),
    path('patient_delete_request/', patient_delete_request),
    path('', index1),
    path('admin_patient_donated_list/', admin_patient_donated_list),
    path('admin_patient_donated_list/', admin_patient_donated_list),
    path('admin_patient_donated_list/', admin_patient_donated_list),
    
    
    
]
