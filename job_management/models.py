from django.db import models

class JobDescription(models.Model):
    job_title = models.CharField(max_length=255)
    responsibilities = models.TextField()
    skills_required = models.TextField()
    experience = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title

class InterviewQuestion(models.Model):
    job = models.ForeignKey(JobDescription, related_name='interview_questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    is_technical = models.BooleanField(default=False)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.question_text
