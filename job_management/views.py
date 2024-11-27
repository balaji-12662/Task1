from django.shortcuts import render, redirect
from .models import JobDescription, InterviewQuestion
from .froms import JobDescriptionForm,InterviewQuestionForm
from django.http import JsonResponse

def job_description_view(request):
    if request.method == 'POST':
        form = JobDescriptionForm(request.POST)
        if form.is_valid():
            job = form.save()  # Save the job description instance
            # Redirect to the view_job_description URL and pass the job_id
            return redirect('view_job_description', job_id=job.id)
    else:
        form = JobDescriptionForm()
    return render(request, 'job_management/job_description_form.html', {'form': form})

def view_job_description(request, job_id):
    job = JobDescription.objects.get(id=job_id)
    interview_questions = InterviewQuestion.objects.filter(job=job)
    return render(request, 'job_management/view_job_description.html', {'job': job, 'interview_questions': interview_questions})

def edit_interview_questions(request, job_id):
    job = JobDescription.objects.get(id=job_id)
    if request.method == 'POST':
        form = InterviewQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.job = job
            question.save()
            return redirect('view_job_description', job_id=job.id)
    else:
        form = InterviewQuestionForm()
    return render(request, 'job_management/edit_interview_questions.html', {'form': form, 'job': job})

    
# from django.shortcuts import render
# from .scraper import scrape_job_description

# def job_search_view(request):
#     job_title = None
#     job_data = None
#     error_message = None
    
#     if request.method == 'GET':
#         # Check if 'job_title' exists in the GET request
#         job_title = request.GET.get('job_title')
        
#         print(f"Received job_title: {job_title}")  # Add logging to debug
        
#         if job_title:
#             # Call the scraper function
#             job_data = scrape_job_description(job_title)
            
#             if isinstance(job_data, str) and job_data.startswith('Failed'):
#                 error_message = job_data  # If an error occurs during scraping
#             elif job_data == "No job listings found.":
#                 error_message = job_data  # If no listings are found
#         else:
#             error_message = "Please enter a job title to search."
    
#     return render(request, 'job_search_results.html', {
#         'job_title': job_title,
#         'job_data': job_data,
#         'error_message': error_message
#     })

from django.shortcuts import render
from .scraper import scrape_job_description

def job_search_view(request):
    job_title = None
    job_data = None
    error_message = None
    
    # Check if the 'job_title' parameter is present in the GET request
    if request.method == 'GET':
        job_title = request.GET.get('job_title', None)  # Retrieve the job_title or None if not found
        
        if job_title:
            # If job_title is provided, call the scraper function
            job_data = scrape_job_description(job_title)
            
            # If the scraper returns an error message
            if isinstance(job_data, str) and job_data.startswith('Failed'):
                error_message = job_data
            elif job_data == "No job listings found.":
                error_message = job_data
        else:
            # If no job_title is provided, set an error message
            error_message = "Please enter a job title to search."
    
    return render(request, 'job_search_results.html', {
        'job_title': job_title,
        'job_data': job_data,
        'error_message': error_message
    })
