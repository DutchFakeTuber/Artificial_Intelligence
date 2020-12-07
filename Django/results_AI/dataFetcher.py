from django.db import models
from .models import ResultsSurvey, ResultsDataset

class DatasetFetcher():
    def QuestionOne(self):
        # Set all counters to zero
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_1', flat=True)
        # For loop for counting the amount of answers
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_1 = [answer_3, answer_2, answer_1]
        return question_1
    
    def QuestionTwo(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_2', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_2 = [answer_3, answer_2, answer_1]
        return question_2

    def QuestionThree(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_3', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_3 = [answer_3, answer_2, answer_1]
        return question_3

    def QuestionFour(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_4', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_4 = [answer_3, answer_2, answer_1]
        return question_4

    def QuestionFive(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_5', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_5 = [answer_3, answer_2, answer_1]
        return question_5

    def QuestionSix(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_6', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_6 = [answer_3, answer_2, answer_1]
        return question_6

    def QuestionSeven(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_7', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_7 = [answer_3, answer_2, answer_1]
        return question_7

    def QuestionEight(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_8', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_8 = [answer_3, answer_2, answer_1]
        return question_8

    def QuestionNine(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_9', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_9 = [answer_3, answer_2, answer_1]
        return question_9

    def QuestionTen(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_10', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_10 = [answer_3, answer_2, answer_1]
        return question_10

    def QuestionEleven(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_11', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_11 = [answer_3, answer_2, answer_1]
        return question_11

    def QuestionTwelve(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsDataset.objects.values_list('question_12', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_12 = [answer_3, answer_2, answer_1]
        return question_12

class SurveyFetcher():
    def FetchAllData(self):
        data = SurveyFetcher()
        question_1 = data.QuestionOne()
        question_2 = data.QuestionTwo()
        question_3 = data.QuestionThree()
        question_4 = data.QuestionFour()
        question_5 = data.QuestionFive()
        question_6 = data.QuestionSix()
        question_7 = data.QuestionSeven()
        question_8 = data.QuestionEight()
        question_9 = data.QuestionNine()
        question_10 = data.QuestionTen()
        question_11 = data.QuestionEleven()
        question_12 = data.QuestionTwelve()
        questionsSurvey = [
            question_1, question_2, question_3,
            question_4, question_5, question_6,
            question_7, question_8, question_9,
            question_10, question_11, question_12
        ]
        return questionsSurvey

    def QuestionOne(self):
        # Set all counters to zero
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_1', flat=True)
        # For loop for counting the amount of answers
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_1 = [answer_3, answer_2, answer_1]
        return question_1
    
    def QuestionTwo(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_2', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_2 = [answer_3, answer_2, answer_1]
        return question_2

    def QuestionThree(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_3', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_3 = [answer_3, answer_2, answer_1]
        return question_3

    def QuestionFour(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_4', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_4 = [answer_3, answer_2, answer_1]
        return question_4

    def QuestionFive(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_5', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_5 = [answer_3, answer_2, answer_1]
        return question_5

    def QuestionSix(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_6', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_6 = [answer_3, answer_2, answer_1]
        return question_6

    def QuestionSeven(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_7', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_7 = [answer_3, answer_2, answer_1]
        return question_7

    def QuestionEight(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_8', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_8 = [answer_3, answer_2, answer_1]
        return question_8

    def QuestionNine(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_9', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_9 = [answer_3, answer_2, answer_1]
        return question_9

    def QuestionTen(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_10', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_10 = [answer_3, answer_2, answer_1]
        return question_10

    def QuestionEleven(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_11', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_11 = [answer_3, answer_2, answer_1]
        return question_11

    def QuestionTwelve(self):
        answer_1 = 0
        answer_2 = 0
        answer_3 = 0
        answers = ResultsSurvey.objects.values_list('question_12', flat=True)
        for x in answers:
            if x == 0.0:
                answer_1 += 1
            if x == 0.5:
                answer_2 += 1
            if x == 1.0:
                answer_3 += 1
            if x == None or x == '':
                pass
        question_12 = [answer_3, answer_2, answer_1]
        return question_12

class DatasetAndSurveyCounter():
    def FetchAllData(self):
        data = DatasetAndSurveyCounter()
        question_1_total = data.QuestionOne()
        question_2_total = data.QuestionTwo()
        question_3_total = data.QuestionThree()
        question_4_total = data.QuestionFour()
        question_5_total = data.QuestionFive()
        question_6_total = data.QuestionSix()
        question_7_total = data.QuestionSeven()
        question_8_total = data.QuestionEight()
        question_9_total = data.QuestionNine()
        question_10_total = data.QuestionTen()
        question_11_total = data.QuestionEleven()
        question_12_total = data.QuestionTwelve()
        questionsDatasetAndSurvey = [
            question_1_total, question_2_total, question_3_total,
            question_4_total, question_5_total, question_6_total,
            question_7_total, question_8_total, question_9_total,
            question_10_total, question_11_total, question_12_total
        ]
        return questionsDatasetAndSurvey

    def QuestionOne(self):
        question_1_dataset = DatasetFetcher().QuestionOne()
        question_1_survey = SurveyFetcher().QuestionOne()
        question_1_total = [x + y if y != None else x+0 for x, y in zip(question_1_dataset, question_1_survey)]
        return question_1_total

    def QuestionTwo(self):
        question_2_dataset = DatasetFetcher().QuestionTwo()
        question_2_survey = SurveyFetcher().QuestionTwo()
        question_2_total = [x + y if y != None else x+0 for x, y in zip(question_2_dataset, question_2_survey)]
        return question_2_total

    def QuestionThree(self):
        question_3_dataset = DatasetFetcher().QuestionThree()
        question_3_survey = SurveyFetcher().QuestionThree()
        question_3_total = [x + y if y != None else x+0 for x, y in zip(question_3_dataset, question_3_survey)]
        return question_3_total

    def QuestionFour(self):
        question_4_dataset = DatasetFetcher().QuestionFour()
        question_4_survey = SurveyFetcher().QuestionFour()
        question_4_total = [x + y if y != None else x+0 for x, y in zip(question_4_dataset, question_4_survey)]
        return question_4_total

    def QuestionFive(self):
        question_5_dataset = DatasetFetcher().QuestionFive()
        question_5_survey = SurveyFetcher().QuestionFive()
        question_5_total = [x + y if y != None else x+0 for x, y in zip(question_5_dataset, question_5_survey)]
        return question_5_total

    def QuestionSix(self):
        question_6_dataset = DatasetFetcher().QuestionSix()
        question_6_survey = SurveyFetcher().QuestionSix()
        question_6_total = [x + y if y != None else x+0 for x, y in zip(question_6_dataset, question_6_survey)]
        return question_6_total

    def QuestionSeven(self):
        question_7_dataset = DatasetFetcher().QuestionSeven()
        question_7_survey = SurveyFetcher().QuestionSeven()
        question_7_total = [x + y if y != None else x+0 for x, y in zip(question_7_dataset, question_7_survey)]
        return question_7_total

    def QuestionEight(self):
        question_8_dataset = DatasetFetcher().QuestionEight()
        question_8_survey = SurveyFetcher().QuestionEight()
        question_8_total = [x + y if y != None else x+0 for x, y in zip(question_8_dataset, question_8_survey)]
        return question_8_total

    def QuestionNine(self):
        question_9_dataset = DatasetFetcher().QuestionNine()
        question_9_survey = SurveyFetcher().QuestionNine()
        question_9_total = [x + y if y != None else x+0 for x, y in zip(question_9_dataset, question_9_survey)]
        return question_9_total

    def QuestionTen(self):
        question_10_dataset = DatasetFetcher().QuestionTen()
        question_10_survey = SurveyFetcher().QuestionTen()
        question_10_total = [x + y if y != None else x+0 for x, y in zip(question_10_dataset, question_10_survey)]
        return question_10_total

    def QuestionEleven(self):
        question_11_dataset = DatasetFetcher().QuestionEleven()
        question_11_survey = SurveyFetcher().QuestionEleven()
        question_11_total = [x + y if y != None else x+0 for x, y in zip(question_11_dataset, question_11_survey)]
        return question_11_total

    def QuestionTwelve(self):
        question_12_dataset = DatasetFetcher().QuestionTwelve()
        question_12_survey = SurveyFetcher().QuestionTwelve()
        question_12_total = [x + y if y != None else x+0 for x, y in zip(question_12_dataset, question_12_survey)]
        return question_12_total

def Print(self):
    defines = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]
    dataset = "ResultsDataset" # ResultsDataset and ResultsSurvey are possible
    for x, y in zip(range(12), defines):
        print(f"    def Question{y}(self):")
        print(f"        answer_1 = 0")
        print(f"        answer_2 = 0")
        print(f"        answer_3 = 0")
        print(f"        answers = {dataset}.objects.values_list('question_{x+1}', flat=True)")
        print(f"        for x in answers:")
        print(f"            if x == 0.0:")
        print(f"                answer_1 += 1")
        print(f"            if x == 0.5:")
        print(f"                answer_2 += 1")
        print(f"            if x == 1.0:")
        print(f"                answer_3 += 1")
        print(f"            if x == None or x == '':")
        print(f"                pass")
        print(f"        question_{x+1} = [answer_1, answer_2, answer_3]")
        print(f"        return question_{x+1}")

def Print(self):
        defines = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]
        for x, y in zip(range(12), defines):
            print(f"    def Question{y}(self):")
            print(f"        question_{x+1}_dataset = DatasetFetcher().Question{y}")
            print(f"        question_{x+1}_survey = SurveyFetcher().Question{y}")
            print(f"        question_{x+1}_total = [x + y if y != None else x+0 for x, y in zip(question_{x+1}_dataset, question_{x+1}_survey)]")
            print(f"        return question_{x+1}_total")