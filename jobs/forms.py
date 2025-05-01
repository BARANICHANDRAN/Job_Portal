from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'job_title', 'company', 'location', 'job_type', 'min_salary', 'max_salary',
            'description', 'requirements', 'responsibilities', 'application_deadline', 'company_logo'
        ]
        widgets = {
            'application_deadline': forms.SelectDateWidget(years=range(2025, 2031)),
        }
    