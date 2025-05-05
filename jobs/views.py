from django.shortcuts import render, render_to_response, get_object_or_404

from django.contrib.auth.decorators import login_required


from models import Job, JobForm
# Create your views here.

@login_required
def newJob(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            return render(request, 'loads/broker.html')
    else:
        form = JobForm()
    return render(request, 'jobs/newJob.html', {'form':form})

@login_required                                                                 
def listJobs(request):                                                      
    jobs = Job.objects.order_by('job_name')                         
    return render(request, 'jobs/jobList.html', {'jobs': jobs}) 
                                                                                
@login_required                                                                 
def jobDetail(request, pk):                                                 
    job = get_object_or_404(Job, pk=pk)                                 
    return render(request, 'jobs/jobDetail.html', {'job': job}) 

@login_required
def jobEdit(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            return render(request, 'jobs/jobDetail.html', {'job':job})
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/jobEdit.html', {'form':form})    
