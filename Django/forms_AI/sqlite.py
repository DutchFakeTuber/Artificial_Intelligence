import sqlite3

database = "C:/Users/Sybrand/Desktop/AI/Django/db.sqlite3"

connector = sqlite3.connect(database)
cursor = connector.cursor()

def checkTable():
    cursor.execute("SELECT * FROM forms_AI_questions")
    data = cursor.fetchall()

    for x in data:
        print(x)

    connector.close()

# All questions used in the survey
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

def fillData():
    questions = ["Do you have a family history of mental illness?", "Have you ever sought treatment for a mental health disorder from a mental health professional?", "Do you know local or online resources to seek help for a mental health issue?", "Are you aware of the options for mental health care provided by your current employer?", "Did your employer ever formally discuss mental health (as part of a wellness campaign or other official communication)?", "Did your employer provide resources to learn more about mental health disorders and how to seek help?", "Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources with your employer?", "Have you had a mental health disorder in the past?", "Do you currently have a mental health disorder?", "Did you ever discuss your mental health with your current employer?", "Did you ever discuss your mental health with a current coworker(s)?", "Did you hear of/or observe negative consequences for co-workers with mental health issues in your current workplace?"]
    answer_1 = ["Yes", "Yes", "Yes, I know several", "I was aware of some", "None did", "None did", "Yes, always", "Yes", "Yes", "Yes", "Yes", "Yes, all of them"]
    answer_2 = ["No", "No", "I know some", "Yes, I was aware of all of them", "Some did", "Some did", "Sometimes", "Possibly", "Possibly", "No", "No", "Some of them"]
    answer_3 = ["I don't know", None, "No, I don't know any", "No, I only became aware later", "Yes, they all did", "Yes, they all did", "No", "Sometimes", "Sometimes", None, None, "None of them"]
    answer_4 = [None, None, None, None, None, None, None, "No", "No", None, None, None]

    for a, b, c, d, e in zip(questions, answer_1, answer_2, answer_3, answer_4):
        command = "INSERT INTO forms_AI_questions (question, answer_1, answer_2, answer_3, answer_4) VALUES (?, ?, ?, ?, ?)"
        values = (a, b, c, d, e)
        cursor.execute(command, values)
        connector.commit()
    
    cursor.execute("SELECT * FROM forms_AI_questions")
    data = cursor.fetchall()
    for x in data:
        print(x)
    
    connector.close()

def main():
    # fillData()
    checkTable()

if __name__ == "__main__":
    main()