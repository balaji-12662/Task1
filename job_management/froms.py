# job_management/forms.py
from django import forms
from .models import JobDescription,InterviewQuestion

class JobDescriptionForm(forms.ModelForm):
    class Meta:
        model = JobDescription
        fields = ['job_title', 'responsibilities', 'skills_required', 'experience']


class InterviewQuestionForm(forms.ModelForm):
    class Meta:
        model = InterviewQuestion
        fields = ['job', 'question_text','is_technical','answer']
