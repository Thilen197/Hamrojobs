from django.contrib import admin
from jobs.models import Jobs
# Register your models here
class jobAdmin(admin.ModelAdmin):
    list_display = ('job_name','job_address','contact_number','jobs_description')

admin.site.register(Jobs,jobAdmin)

