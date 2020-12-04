import sqlite3

"""
This sqlite program is made solely for injecting new data into the database if something went wrong.
"""

database = "C:/Users/Sybrand/Desktop/AI/Django/db.sqlite3"

connector = sqlite3.connect(database)
cursor = connector.cursor()

# Function for reading table 'forms_AI_questions
def checkTable():
    cursor.execute("SELECT * FROM forms_AI_questions")
    # Fetch all rows from table
    data = cursor.fetchall()

    # Print one row at a time
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
    "Question_1":  ["Yes", "No", "I don't know", None],
    "Question_2":  ["Yes", "No", None, None],
    "Question_3":  ["Yes, I know several", "I know some", "No, I don't know any", None],
    "Question_4":  ["I was aware of some", "Yes, I was aware of all of them", "No, I only became aware later", None],
    "Question_5":  ["None did", "Some did", "Yes, they all did", None],
    "Question_6":  ["None did", "Some did", "Yes, they all did", None],
    "Question_7":  ["Yes, always", "Sometimes", "No", None],
    "Question_8":  ["Yes", "Possibly", "Sometimes", "No"],
    "Question_9":  ["Yes", "Possibly", "Sometimes", "No"],
    "Question_10": ["Yes", "No", None, None],
    "Question_11": ["Yes", "No", None, None],
    "Question_12": ["Yes, all of them", "Some of them", "None of them", None],
}

def fillData():
    # Making arrays with data for the database.
    questions = [
        Questions_Survey["Question_1"],
        Questions_Survey["Question_2"],
        Questions_Survey["Question_3"],
        Questions_Survey["Question_4"],
        Questions_Survey["Question_5"],
        Questions_Survey["Question_6"],
        Questions_Survey["Question_7"],
        Questions_Survey["Question_8"],
        Questions_Survey["Question_9"],
        Questions_Survey["Question_10"],
        Questions_Survey["Question_11"],
        Questions_Survey["Question_12"],
    ]
    answer_1 = [
        Questions_Survey["Question_1"][0],
        Questions_Survey["Question_2"][0],
        Questions_Survey["Question_3"][0],
        Questions_Survey["Question_4"][0],
        Questions_Survey["Question_5"][0],
        Questions_Survey["Question_6"][0],
        Questions_Survey["Question_10"][0],
        Questions_Survey["Question_11"][0],
        Questions_Survey["Question_12"][0],
    ]
    answer_2 = [
        Questions_Survey["Question_1"][1],
        Questions_Survey["Question_2"][1],
        Questions_Survey["Question_3"][1],
        Questions_Survey["Question_4"][1],
        Questions_Survey["Question_5"][1],
        Questions_Survey["Question_6"][1],
        Questions_Survey["Question_10"][1],
        Questions_Survey["Question_11"][1],
        Questions_Survey["Question_12"][1],
    ]
    answer_3 = [
        Questions_Survey["Question_1"][2],
        Questions_Survey["Question_2"][2],
        Questions_Survey["Question_3"][2],
        Questions_Survey["Question_4"][2],
        Questions_Survey["Question_5"][2],
        Questions_Survey["Question_6"][2],
        Questions_Survey["Question_10"][2],
        Questions_Survey["Question_11"][2],
        Questions_Survey["Question_12"][2],
    ]
    answer_4 = [
        Questions_Survey["Question_1"][3],
        Questions_Survey["Question_2"][3],
        Questions_Survey["Question_3"][3],
        Questions_Survey["Question_4"][3],
        Questions_Survey["Question_5"][3],
        Questions_Survey["Question_6"][3],
        Questions_Survey["Question_10"][3],
        Questions_Survey["Question_11"][3],
        Questions_Survey["Question_12"][3],
    ]

    # Injecting data into the database table 'forms_AI_questions' one line at a time.
    for a, b, c, d, e in zip(questions, answer_1, answer_2, answer_3, answer_4):
        command = "INSERT INTO forms_AI_questions (question, answer_1, answer_2, answer_3, answer_4) VALUES (?, ?, ?, ?, ?)"
        values = (a, b, c, d, e)
        cursor.execute(command, values)
        connector.commit()
    
    # Read table 'forms_AI_questions'
    cursor.execute("SELECT * FROM forms_AI_questions")
    # Fetch all lines
    data = cursor.fetchall()
    # Print one line at a time
    for x in data:
        print(x)
    
    #Closing connection with database
    connector.close()

def main():
    # fillData()
    checkTable()

if __name__ == "__main__":
    main()