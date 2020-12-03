import sqlite3
 

ANSWERTEXT = 0
SURVEY_ID = 1
USER_ID = 2
QUESTION_ID = 3
 
database = "mental_health.sqlite"
 
connector = sqlite3.connect(database)
cursor = connector.cursor()
 
cursor.execute('SELECT * FROM Answer')
data = cursor.fetchall()

#Transformation for question one
print([(int(answer[ANSWERTEXT]) - 15) / 59 if (int(answer[QUESTION_ID]) == 1 and int(answer[ANSWERTEXT]) >= 15 and int(answer[ANSWERTEXT]) <= 74) else None for answer in data])
