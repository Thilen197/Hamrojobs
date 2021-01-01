from django import forms
from jobs.models import Jobs

class Jobsform(forms.ModelForm) :
    class meta:
        model = Jobs
        #fields=("jobs_name")
        fields= "_all_"
