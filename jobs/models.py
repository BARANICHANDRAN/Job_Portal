from django.db import models

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]

    job_title = models.CharField(max_length=200)  
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    min_salary = models.IntegerField(default=0)
    max_salary = models.IntegerField(default=0)
    description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField()
    application_deadline = models.DateField()
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)

    def __str__(self):
        return self.job_title
