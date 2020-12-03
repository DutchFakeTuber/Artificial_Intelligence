def numbersOnly():
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',', str(data))))
    print(newData.replace(",,", ", "))

def textOnly():
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))

def negativeNumbersToo():
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))

def textAndNumbers():
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))

def apostrophesInText():
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")

print("\nDID NOT FILTER THE BRACKETS BECAUSE OF THE BRACKETS IN TEXT")
print("\nPERSONAL EXPERIENCES OF THE PEOPLE, CANNOT BE USED.")
