from django.shortcuts import render
from results_AI.models import ResultsTable
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms
from .models import Questions

# All questions used for the survey
Questions_Survey = {
    "Question_1":  "Do you have a family history of mental illness?",
    "Question_2":  "Have you ever sought treatment for a mental health disorder from a mental health professional?",
    "Question_3":  "Do you know local or online resources to seek help for a mental health issue?",
    "Question_4":  "Are you aware of the options for mental health care provided by your current employer?",
    "Question_5":  "Did your employer ever formally discuss mental health (as part of a wellness campaign or other official communication)?",
    "Question_6":  "Did your employer provide resources to learn more about mental health disorders and how to seek help?",
    "Question_7":  "Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources with your employer?",
    "Question_8":  "Have you had a mental health disorder in the past?",
    "Question_9":  "Do you currently have a mental health disorder?",
    "Question_10": "Did you ever discuss your mental health with your current employer?",
    "Question_11": "Did you ever discuss your mental health with a current coworker(s)?",
    "Question_12": "Did you hear of/or observe negative consequences for co-workers with mental health issues in your current workplace?",
}
# All answers of each question
Answer_Question = {
    "Question_1":  ["Yes", "No", "I don't know"],
    "Question_2":  ["Yes", "No"],
    "Question_3":  ["Yes, I know several", "I know some", "No, I don't know any"],
    "Question_4":  ["I was aware of some", "Yes, I was aware of all of them", "No, I only became aware later"],
    "Question_5":  ["None did", "Some did", "Yes, they all did"],
    "Question_6":  ["None did", "Some did", "Yes, they all did"],
    "Question_7":  ["Yes, always", "Sometimes", "No"],
    "Question_8":  ["Yes", "Possibly", "Sometimes", "No"],
    "Question_9":  ["Yes", "Possibly", "Sometimes", "No"],
    "Question_10": ["Yes", "No"],
    "Question_11": ["Yes", "No"],
    "Question_12": ["Yes, all of them", "Some of them", "None of them"],
}

# Function for the forms.html file
def index(request):
    # Fetch all data from the Questions class in models.py (database)
    questionTextRaw = Questions.objects.all()
    # Fetch all RadioButton functions
    answers_1 = forms.RadioButtons_questionOne()
    answers_2 = forms.RadioButtons_questionTwo()
    answers_3 = forms.RadioButtons_questionThree()
    answers_4 = forms.RadioButtons_questionFour()
    answers_5 = forms.RadioButtons_questionFive()
    answers_6 = forms.RadioButtons_questionSix()
    answers_7 = forms.RadioButtons_questionSeven()
    answers_8 = forms.RadioButtons_questionEight()
    answers_9 = forms.RadioButtons_questionNine()
    answers_10 = forms.RadioButtons_questionTen()
    answers_11 = forms.RadioButtons_questionEleven()
    answers_12 = forms.RadioButtons_questionTwelve()
    # Put all RadioButton functions into an array
    totalAnswers = [answers_1, answers_2, answers_3, answers_4, answers_5, answers_6, answers_7, answers_8, answers_9, answers_10, answers_11, answers_12]
    # Put all data into a dictionary
    information = {
        'questions': questionTextRaw,
        'answers': totalAnswers,
    }
    # If the Submit button is pressed:
    if request.method == 'POST':
        # Array with all names of the RadioButton elements
        allAnswers = ["question_1", "question_2", "question_3", "question_4", "question_5", "question_6", "question_7", "question_8", "question_9", "question_10", "question_11", "question_12"]
        # Fetch all values of the RadioButton elements and put it into an array
        answers = [request.POST.get(x) for x in allAnswers]

        # """ # BEGIN - For testing purposes only;
        # Print all answers into the terminal
        # for x in answers:
            # print(x)
        
        # Return a HTTP Response and put all fetched data there
        return HttpResponse((f'Question {x+1} is: ' + answers[x] + ' ') for x in range(12))
        # """ # END - For testing purposes only
    
    # Send all data to the forms.html file to be used there
    return render(request, 'forms_AI_index.html', information)
    