from django import forms
from django.utils.safestring import mark_safe

# All answers of each question and their respective values
Answer_Question = {
    "Question_1":  [
        0,      "No",
        0.5,    "I don't know",
        1,      "Yes"
        ],
    "Question_2":  [
        0,      "No",
        1,      "Yes"
        ],
    "Question_3":  [
        0,      "No, I don't know any",
        0.5,    "I know some",
        1,      "Yes, I know several"
        ],
    "Question_4":  [
        0,      "No, I only became aware later",
        0.5,    "I was aware of some",
        1,      "Yes, I was aware of all of them"
        ],
    "Question_5":  [
        0,      "None did",
        0.5,    "Some did",
        1,      "Yes, they all did"
        ],
    "Question_6":  [
        0,      "None did",
        0.5,    "Some did",
        1,      "Yes, they all did"
        ],
    "Question_7":  [
        0,      "No",
        0.5,    "Sometimes",
        1,      "Yes, always"
        ],
    "Question_8":  [
        0,      "No",
        0.5,    "Possibly",
        0.5,    "Maybe",
        1,      "Yes"
        ],
    "Question_9":  [
        0,      "No",
        0.5,    "Possibly",
        0.5,    "Maybe",
        1,      "Yes"
        ],
    "Question_10": [
        0,      "No",
        1,      "Yes"
        ],
    "Question_11": [
        0,      "No",
        1,      "Yes"
        ],
    "Question_12": [
        0,      "None of them",
        0.5,    "Some of them",
        1,      "Yes, all of them"
        ],
}

class RadioButtons_questionOne(forms.Form):
    question_1 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_1'][0], Answer_Question['Question_1'][1]),
            (Answer_Question['Question_1'][2], Answer_Question['Question_1'][3]),
            (Answer_Question['Question_1'][4], Answer_Question['Question_1'][5]),
        ],
        required=True,
        widget=forms.RadioSelect
    )
class RadioButtons_questionTwo(forms.Form):
    question_2 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_2'][0], Answer_Question['Question_2'][1]),
            (Answer_Question['Question_2'][2], Answer_Question['Question_2'][3]),
        ],
        required=True,
        widget=forms.RadioSelect
    )
class RadioButtons_questionThree(forms.Form):
    question_3 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_3'][0], Answer_Question['Question_3'][1]),
            (Answer_Question['Question_3'][2], Answer_Question['Question_3'][3]),
            (Answer_Question['Question_3'][4], Answer_Question['Question_3'][5]),
        ],
        required=True,
        widget=forms.RadioSelect
    )
class RadioButtons_questionFour(forms.Form):
    question_4 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_4'][0], Answer_Question['Question_4'][1]),
            (Answer_Question['Question_4'][2], Answer_Question['Question_4'][3]),
            (Answer_Question['Question_4'][4], Answer_Question['Question_4'][5]),
        ],
        required=True,
        widget=forms.RadioSelect
    )
class RadioButtons_questionFive(forms.Form):
    question_5 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_5'][0], Answer_Question['Question_5'][1]),
            (Answer_Question['Question_5'][2], Answer_Question['Question_5'][3]),
            (Answer_Question['Question_5'][4], Answer_Question['Question_5'][5]),
        ],
        required=True,
        widget=forms.RadioSelect
    )
class RadioButtons_questionSix(forms.Form):
    question_6 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_6'][0], Answer_Question['Question_6'][1]),
            (Answer_Question['Question_6'][2], Answer_Question['Question_6'][3]),
            (Answer_Question['Question_6'][4], Answer_Question['Question_6'][5]),
        ],
        required=True,
        widget=forms.RadioSelect
    )
class RadioButtons_questionSeven(forms.Form):
    question_7 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_7'][0], Answer_Question['Question_7'][1]),
            (Answer_Question['Question_7'][2], Answer_Question['Question_7'][3]),
            (Answer_Question['Question_7'][4], Answer_Question['Question_7'][5]),
        ],
        required=True,
        widget=forms.RadioSelect
    )
class RadioButtons_questionEight(forms.Form):
    question_8 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_8'][0], Answer_Question['Question_8'][1]),
            (Answer_Question['Question_8'][2], Answer_Question['Question_8'][3]),
            (Answer_Question['Question_8'][4], Answer_Question['Question_8'][5]),
            (Answer_Question['Question_8'][6], Answer_Question['Question_8'][7]),
        ],
        required=True,
        widget=forms.RadioSelect
    )
class RadioButtons_questionNine(forms.Form):
    question_9 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_9'][0], Answer_Question['Question_9'][1]),
            (Answer_Question['Question_9'][2], Answer_Question['Question_9'][3]),
            (Answer_Question['Question_9'][4], Answer_Question['Question_9'][5]),
            (Answer_Question['Question_9'][6], Answer_Question['Question_9'][7]),
        ],
        required=True,
        widget=forms.RadioSelect
    )
class RadioButtons_questionTen(forms.Form):
    question_10 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_10'][0], Answer_Question['Question_10'][1]),
            (Answer_Question['Question_10'][2], Answer_Question['Question_10'][3]),
        ],
        required=True,
        widget=forms.RadioSelect
    )
class RadioButtons_questionEleven(forms.Form):
    question_11 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_11'][0], Answer_Question['Question_11'][1]),
            (Answer_Question['Question_11'][2], Answer_Question['Question_11'][3]),
        ],
        widget=forms.RadioSelect
    )
class RadioButtons_questionTwelve(forms.Form):
    question_12 = forms.ChoiceField(
        label='',
        choices=[
            (Answer_Question['Question_12'][0], Answer_Question['Question_12'][1]),
            (Answer_Question['Question_12'][2], Answer_Question['Question_12'][3]),
            (Answer_Question['Question_12'][4], Answer_Question['Question_12'][5]),
        ],
        required=True,
        widget=forms.RadioSelect
    )