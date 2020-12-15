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
question_recommendations = {
    'Question_4': 'Employees are not aware of the options for mental health care provided by their employer, consider informing employees about this.',
    'Question_5': 'Consider discussing mental health formally (as part of a wellness campaign).',
    'Question_6': 'Consider to provide employees with resources to learn more about mental health disorders.',
    'Question_7': 'Consider to procect employees anonymity if they choose to take advantage of mental health or substance abuse treatment.',
    'Question_10': 'Consider talking with employees about their mental health'
}


def get_question_averages():
    answers = [answer.get_result_list() for answer in ResultsSurvey.objects.all()]
    return [mean([answer[i] for answer in answers]) for i in range(12)]


def get_question_recommendations():
    averages = get_question_averages()
    not_recommendable = [0, 1, 2, 7, 8, 10, 11]
    averages_dict = {f'Question_{i + 1}': average for i, average in enumerate(averages) if i not in not_recommendable}
    return averages_dict


def index(request):
    predictions = get_predictions()
    if predictions:
        average = min(100, max(0, int(mean(predictions) * 100)))

        recommendation_averages = get_question_recommendations()
        sorted_recommendations = sorted(recommendation_averages, key=recommendation_averages.get)
        recommendations = [question_recommendations[r] for r in sorted_recommendations]
        recommendations = recommendations[:0 if average < 33 else 2 if average < 66 else 4]

        predictions = [min(100, max(0, int(prediction * 100))) for prediction in predictions]
        averages = [int(mean(predictions[:i + 1]) + 0.5) for i in range(len(predictions))]
    else:
        average = 0
        recommendations = []
        averages = []
    return render(request, 'results_AI_index.html', {
        'average': average,
        'recommendations': recommendations,
        'predictions': predictions,
        'labels': [i + 1 for i in range(len(predictions))],
        'averages': averages,
    })


def get_predictions():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'predict_model')
    model = load_model(filename)
    answers = [answer.get_result_list() for answer in ResultsSurvey.objects.all()]
    print(answers)
    if len(answers) == 0:
        return []
    predictions = [result[0] for result in model.predict(answers)]
    print(predictions)
    return predictions


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
