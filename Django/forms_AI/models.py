from django.db import models

class Questions(models.Model):
    question = models.CharField(max_length=255)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255, blank=True, null=True)
    answer_4 = models.CharField(max_length=255, blank=True, null=True)