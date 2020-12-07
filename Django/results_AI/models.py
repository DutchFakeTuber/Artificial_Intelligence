from django.db import models

# In this case two tables are used; one for the dataset and one for the survey data.
class ResultsDataset(models.Model):
    question_1 = models.FloatField(blank=True, null=True)
    question_2 = models.FloatField(blank=True, null=True)
    question_3 = models.FloatField(blank=True, null=True)
    question_4 = models.FloatField(blank=True, null=True)
    question_5 = models.FloatField(blank=True, null=True)
    question_6 = models.FloatField(blank=True, null=True)
    question_7 = models.FloatField(blank=True, null=True)
    question_8 = models.FloatField(blank=True, null=True)
    question_9 = models.FloatField(blank=True, null=True)
    question_10 = models.FloatField(blank=True, null=True)
    question_11 = models.FloatField(blank=True, null=True)
    question_12 = models.FloatField(blank=True, null=True)

class ResultsSurvey(models.Model):
    question_1 = models.FloatField()
    question_2 = models.FloatField()
    question_3 = models.FloatField()
    question_4 = models.FloatField()
    question_5 = models.FloatField()
    question_6 = models.FloatField()
    question_7 = models.FloatField()
    question_8 = models.FloatField()
    question_9 = models.FloatField()
    question_10 = models.FloatField()
    question_11 = models.FloatField()
    question_12 = models.FloatField()
    dateAndTime = models.DateTimeField(auto_now_add=True)