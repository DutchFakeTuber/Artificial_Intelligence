import sqlite3

database = "mental_health.sqlite"

connector = sqlite3.connect(database)
cursor = connector.cursor()


def fetchTables():
    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()

def filterQuestionOne():
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '1') AND CAST(AnswerText AS INTEGER) BETWEEN 15 AND 74 ORDER BY AnswerText DESC")
    data = cursor.fetchall()
    array = []
    for i in range(len(data)):
        print(array[i])
    connector.commit()

def filterQuestionTwo():
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '3')")
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()

connector.close()
filterQuestionOne()