from django import forms
from .models import *
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor    
        fields = '__all__'
class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor    
        fields = '__all__'
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient    
        fields = '__all__'