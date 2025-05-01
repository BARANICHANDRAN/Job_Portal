from django.shortcuts import render, redirect,get_object_or_404
from .models import Job
from .forms import JobForm

def job_list(request):
    jobs = Job.objects.all()

    title = request.GET.get('title', '')
    location = request.GET.get('location', '')
    job_type = request.GET.get('job_type', '')
    min_salary = request.GET.get('min_salary')
    max_salary = request.GET.get('max_salary')

    if title:
        jobs = jobs.filter(job_title__icontains=title)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if min_salary:
        jobs = jobs.filter(min_salary__gte=int(min_salary))
    if max_salary:
        jobs = jobs.filter(max_salary__lte=int(max_salary))


    return render(request, 'job_list.html', {'jobs': jobs})


def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'job_detail.html', {'job': job})

def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'post_job.html', {'form': form})


def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    return redirect('job_list')
