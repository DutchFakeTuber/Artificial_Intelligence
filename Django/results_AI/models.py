from django.db import models

# In this case one table can be used for all information; dataset and survey data alike.
class ResultsTable(models.Model):
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
    # True = Survey, False = Dataset
    ourSurvey = models.BooleanField()

# In this case two tables are used; one for the dataset and one for the survey data.
class ResultsDataset(models.Model):
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