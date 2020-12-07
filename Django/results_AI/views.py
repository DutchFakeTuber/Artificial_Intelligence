from django.shortcuts import render
from forms_AI.models import Questions
from . import dataFetcher

# Create your views here.
def index(request):
    return render(request, 'results_AI_index.html', {})

def allQuestions(request):
    questionTextRaw = Questions.objects.all()
    information = {
        "dataQuestions": questionTextRaw,
    }
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