from django.db import models
"""
This class is used for the Database of Django.
Whenever the server needs to store data, these functions have to be built first.
Then, the changes must be migrated using 'makemigrations {name folder}', followed by 'migrate'.
"""

#The table Questions
class Questions(models.Model):
    # Column Question with maximum length of 255 characters.
    question = models.CharField(max_length=255)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    # Column answer_3 with maximum length of 255 characters, blank enabled and null enabled as well.
    # Blank is for Django, this is necessary when the program wants to send a 'blank' value to the database;
    # Null is for the Database. This enables the Database to accept Null values.
    answer_3 = models.CharField(max_length=255, blank=True, null=True)
    answer_4 = models.CharField(max_length=255, blank=True, null=True)