from django.shortcuts import render
from forms_AI.models import Questions
from keras.models import load_model
from . import dataFetcher
from statistics import mean
from .models import ResultsSurvey
import tensorflow
import os
import numpy

# Create your views here.


def index(request):
    average = int(get_prediction_average() * 100)
    return render(request, 'results_AI_index.html', {'average': average})


def get_prediction_average():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'predict_model')
    model = load_model(filename)
    answers = [answer.get_result_list() for answer in ResultsSurvey.objects.all()]
    print(answers)
    predictions = [result[0] for result in model.predict(answers)]
    return mean(predictions)


def allQuestions(request):
    questionsSurvey = dataFetcher.SurveyFetcher().FetchAllData()
    information = {f'Question_{i + 1}': questionsSurvey[i] for i in range(12)}

    return render(request, 'results_AI_allQuestions.html', information)


def perQuestion(request):
    questionsSurvey = dataFetcher.SurveyFetcher().FetchAllData()
    questionsDatasetAndSurvey = dataFetcher.DatasetAndSurveyCounter().FetchAllData()

    questionsTextRaw = Questions.objects.all()
    # Put the logic here for counting the amount of answers per question
    # One type of logic with and one without dataset
    information = {
        "dataQuestions": questionsTextRaw,
        "questionsSurvey": questionsSurvey,
        "questionsDatasetAndSurvey": questionsDatasetAndSurvey,
    }
    return render(request, 'results_AI_perQuestion.html', information)


def howDoesItWork(request):
    return render(request, 'results_AI_howDoesItWork.html', {})
