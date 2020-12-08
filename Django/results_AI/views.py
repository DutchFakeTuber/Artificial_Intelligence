from django.shortcuts import render
from forms_AI.models import Questions
from . import dataFetcher

# Create your views here.
def index(request):
    return render(request, 'results_AI_index.html', {})

def allQuestions(request):
    questionsSurvey = dataFetcher.SurveyFetcher().FetchAllData()
    information = {
        "Question_1": questionsSurvey[0],
        "Question_2": questionsSurvey[1],
        "Question_3": questionsSurvey[2],
        "Question_4": questionsSurvey[3],
        "Question_5": questionsSurvey[4],
        "Question_6": questionsSurvey[5],
        "Question_7": questionsSurvey[6],
        "Question_8": questionsSurvey[7],
        "Question_9": questionsSurvey[8],
        "Question_10": questionsSurvey[9],
        "Question_11": questionsSurvey[10],
        "Question_12": questionsSurvey[11],
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