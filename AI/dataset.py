import sqlite3

ANSWERTEXT = 0
SURVEY_ID = 1
USER_ID = 2
QUESTION_ID = 3

TOTAL_QUESTIONS = 105
EXCLUDE_IDS = [3, 4, 50, 51, 59, 61, 63, 71, 73, 75, 82, 84, 86, 87, 89, 103, 115, 116, 117]

questions = {}
questions.update({
    'question_1': {str(i): ((i - 15) / 59) for i in range(15, 75)},
    'question_2': {
        'Female': 0,
        'female': 0,
        'Male': 1,
        'male': 1,
    },
    'question_5': {
        '0': 0,
        '1': 1,
    },
    'question_6': {
        'No': 0,
        "I don't know": 0.5,
        'Yes': 1,
    },
})
questions.update({
    'question_7': questions['question_5'],
    'question_8': {
        '1-5': 0,
        '6-25': 0.2,
        '26-100': 0.4,
        '100-500': 0.6,
        '500-1000': 0.8,
        'More than 1000': 1,
    },
    'question_9': questions['question_5'],
    'question_10': {
        'Yes': 1,
        'No': 0,
    }
})
questions.update({
    'question_11': questions['question_10'],
    'question_12': {
        'No': 0,
        'Maybe': 0.5,
        'Yes': 1,
    },
    'question_13': questions['question_5'],
    'question_14': {
        'No': 0,
        'I am not sure': 0.5,
        'Yes': 1,
    },
    'question_15': questions['question_6']
})
questions.update({
    'question_16': questions['question_15'],
    'question_17': {
        'Very easy': 0,
        'Somewhat easy': 0.2,
        'Neither easy nor difficult': 0.4,
        'Somewhat difficult': 0.6,
        'Difficult': 0.8,
        'Very difficult': 1
    },
    'question_18': questions['question_12'],
    'question_19': questions['question_12'],
    'question_20': questions['question_5'],
    'question_21': {
        "No, I don't know any": 0,
        'I know some': 0.5,
        'Yes, I know several': 1,
    },
    'question_22': questions['question_5'],
    'question_23': {
        'No, none did': 0,
        'Some did': 0.5,
        'Yes, they all did': 1
    },
    'question_24': {
        'No, I only became aware later': 0,
        'I was aware of some': 0.5,
        'Yes, I was aware of all of them': 1,
    },
})
questions.update({
    'question_25': questions['question_23'],
    'question_26': questions['question_23'],
    'question_27': {
        'No': 0,
        'Sometimes': 0.5,
        'Yes, always': 1,
    },
    'question_28': {
        'No, at none of my previous employers': 0,
        'No, none of my previous supervisors': 0,
        'Some of my previous employers': 0.5,
        'Some of my previous supervisors': 0.5,
        'Yes, all of my previous supervisors': 1,
        'Yes, at all of my previous employers': 1,
    },
    'question_29': {
        'No': 0,
        'Maybe': 0.5,
        'Yes': 1,
    },
    'question_30': {
        'Not open at all': 0,
        'Somewhat not open': 0.25,
        'Neutral': 0.5,
        'Somewhat open': 0.75,
        'Very open': 1,
    },
})
questions.update({
    'question_31': questions['question_29'],
    'question_32': {
        'No': 0,
        'Maybe': 0.5,
        'Possibly': 0.5,
        'Yes': 1,
    },
})
questions.update({
    'question_33': questions['question_32'],
    'question_34': {
        'No': 0,
        'Yes': 1,
    },
    'question_48': {
        'Never': 0,
        'Rarely': 1/3,
        'Sometimes': 2/3,
        'Often': 1,
    },
})
questions.update({
    'question_49': questions['question_48'],
    'question_52': {
        "No, because it doesn't matter": 0,
        'No, because it would impact me negatively': 0,
        'Sometimes, if it comes up': 0.5,
        'Yes, always': 1,
    },
})
questions.update({
    'question_53': questions['question_52'],
    'question_54': {
        'Yes': 1,
        'Unsure': 0.5,
        'No': 0,
    },
    'question_55': {
        '1-25%': 0,
        '26-50%': 1/3,
        '51-75%': 2/3,
        '76-100%': 1,
    },
    'question_56': {
        'No': 0,
        'Maybe/Not sure': 0.5,
        'Yes, I experienced': 1,
        'Yes, I observed': 1,
    },
    'question_57': {
        'Physical health': 0,
        'Same level of comfort for each': 0.5,
        'Mental health': 1,
    },
    'question_58': questions['question_5'],
    'question_60': questions['question_5'],
    'question_62': questions['question_5'],
    'question_64': {str(i): i / 10 for i in range(11)}
})
questions.update({
    'question_65': questions['question_64'],
    'question_66': {
        'Negatively': 0,
        'No change': 0.5,
        "I'm not sure": 0.5,
        'Positively': 1,
    }
})
questions.update({
    'question_67': questions['question_66'],
    'question_68': questions['question_5'],
    'question_69': questions['question_57'],
    'question_70': questions['question_5'],
    'question_72': questions['question_5'],
    'question_74': questions['question_5'],
    'question_76': questions['question_64'],
    'question_77': questions['question_64'],
    'question_78': questions['question_5'],
    'question_79': questions['question_5'],
    'question_80': questions['question_64'],
    'question_81': questions['question_64'],
    'question_83': questions['question_56'],
    'question_85': {str(i + 1): i / 4 for i in range(5)},
    'question_88': questions['question_5'],
    'question_90': questions['question_29'],
    'question_91': {
        'No': 0,
        "I don't know": 0.5,
        "Don't know": 0.5,
        'Yes': 1,
    },
    'question_92': questions['question_48'],
    'question_93': questions['question_10'],
    'question_94': {
        'Yes': 1,
        'Unsure': 0.5,
        'No': 0,
    },
    'question_95': {
        'Yes': 1,
        "Don't know": 0.5,
        'No': 0,
    },
})
questions.update({
    'question_96': questions['question_95'],
    'question_97': {
        'Very easy': 0,
        'Somewhat easy': 1/3,
        'Somewhat difficult': 2/3,
        'Very difficult': 1
    },
    'question_98': questions['question_29'],
    'question_99': {
        'No': 0,
        'Some of them': 0.5,
        'Yes': 1,
    },
})
questions.update({
    'question_100': questions['question_99'],
    'question_101': questions['question_29'],
    'question_102': questions['question_10'],
    'question_104': questions['question_29'],
    'question_105': questions['question_10'],
    'question_106': {
        'No': 0,
        "I'm not sure": 0.5,
        'Yes': 1,
    },
})
questions.update({
    'question_107': questions['question_106'],
    'question_108': {
        'None of them': 0,
        'Some of them': 0.5,
        'Yes, all of them': 1,
    },
})
questions.update({
    'question_109': questions['question_108'],
    'question_110': {
        'No, at none of my previous employers': 0,
        'Some of my previous employers': 0.5,
        'Yes, at all of my previous employers': 1,
    },
    'question_111': questions['question_27'],
    'question_112': {
        'None of them': 0,
        'Some of them': 0.5,
        'Yes, all of them': 1,
    },
    'question_113': {
        "No, I don't think it would": 0,
        'No, it has not': 0,
        'Maybe': 0.5,
        'Yes, I think it would': 1,
        'Yes, it has': 1,
    },
    'question_114': {
        "No, I don't think they would": 0,
        'No, they do not': 0,
        'Maybe': 0.5,
        'Yes, they do': 1,
        'Yes, I think they would': 1,
    },
    'question_118': {
        'Sometimes': 0.5,
        'Never': 0,
        'Always': 1,
    },
})


def get_dataset():
    database = "mental_health.sqlite"

    connector = sqlite3.connect(database)
    cursor = connector.cursor()

    cursor.execute('SELECT * FROM Answer')
    data = cursor.fetchall()

    cursor.execute('SELECT UserID From Answer')
    user_ids = set(cursor.fetchall())

    result = [[None for i in range(TOTAL_QUESTIONS)] for user_id in user_ids]

    def result_assign(answer, val):
        result[answer[USER_ID] - 1][answer[QUESTION_ID] - (1 if answer[QUESTION_ID] < 35 else 14)] = val

    def result_assign_from_dict(answer, question_dict):
        result_assign(answer, question_dict[str(answer[ANSWERTEXT])] if str(answer[ANSWERTEXT]) in question_dict else None)

    for answer in data:
        if answer[QUESTION_ID] not in EXCLUDE_IDS:
            result_assign_from_dict(answer, questions[f'question_{answer[QUESTION_ID]}'])

    return result
