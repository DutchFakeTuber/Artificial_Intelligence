import sqlite3
database = "mental_health.sqlite"

connector = sqlite3.connect(database)
cursor = connector.cursor()
#Wordt meegenomen
def filterQuestion1(questionNumber=None):
    # What is your age?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s') AND CAST(AnswerText AS INTEGER) BETWEEN 15 AND 74 ORDER BY AnswerText DESC" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion2(questionNumber=None):
    # What is your gender?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nCANNOT BE TRANSFORMED INTO 0.0 TO 1.0")
    return

#Overgeslagen
def filterQuestion3(questionNumber=None):
    # What country do you live in?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = cursor.fetchall()
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ","))
    connector.commit()
    print("\nCANNOT BE TRANSFORMED INTO 0.0 TO 1.0")
    return

#Overgeslagen
def filterQuestion4(questionNumber=None):
    # If you live in the United States, which state or territory do you live in?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = cursor.fetchall()
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ","))
    connector.commit()
    print("\nCANNOT BE TRANSFORMED INTO 0.0 TO 1.0")
    return

#Wordt meegenomen
def filterQuestion5(questionNumber=None):
    # Are you self-employed?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion6(questionNumber=None):
    # Do you have a family history of mental illness?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion7(questionNumber=None):
    # Have you ever sought treatment for a mental health disorder from a mental health professional?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion8(questionNumber=None):
    # How many employees does your company or organization have?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion9(questionNumber=None):
    # Is your employer primarily a tech company/organization?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion10(questionNumber=None):
    # Does your employer provide mental health benefits as part of healthcare coverage?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion11(questionNumber=None):
    # Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources provided by your employer?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion12(questionNumber=None):
    # Would you bring up a mental health issue with a potential employer in an interview?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion13(questionNumber=None):
    # Is your primary role within your company related to tech/IT?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion14(questionNumber=None):
    # Do you know the options for mental health care available under your employer-provided health coverage?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion15(questionNumber=None):
    # Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion16(questionNumber=None):
    # Does your employer offer resources to learn more about mental health disorders and options for seeking help?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion17(questionNumber=None):
    # If a mental health issue prompted you to request a medical leave from work, how easy or difficult would it be to ask for that leave?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion18(questionNumber=None):
    # Would you feel comfortable discussing a mental health issue with your coworkers?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion19(questionNumber=None):
    # Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion20(questionNumber=None):
    # Do you have medical coverage (private insurance or state-provided) that includes treatment of mental health disorders?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion21(questionNumber=None):
    # Do you know local or online resources to seek help for a mental health issue?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion22(questionNumber=None):
    # Do you have previous employers?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion23(questionNumber=None):
    # Have your previous employers provided mental health benefits?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion24(questionNumber=None):
    # Were you aware of the options for mental health care provided by your previous employers?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    print(data)
    print("\nDID NOT FILTER THE BRACKETS BECAUSE OF THE BRACKETS IN TEXT")
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion25(questionNumber=None):
    # Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion26(questionNumber=None):
    # Did your previous employers provide resources to learn more about mental health disorders and how to seek help?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion27(questionNumber=None):
    # Was your anonymity protected if you chose to take advantage of mental health or substance abuse treatment resources with previous employers?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion28(questionNumber=None):
    # Would you have been willing to discuss your mental health with your direct supervisor(s)?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion29(questionNumber=None):
    # Would you be willing to bring up a physical health issue with a potential employer in an interview?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion30(questionNumber=None):
    # How willing would you be to share with friends and family that you have a mental illness?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    print(data)
    print("\nDID NOT FILTER THE BRACKETS BECAUSE OF THE BRACKETS IN TEXT")
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion31(questionNumber=None):
    # Have your observations of how another individual who discussed a mental health disorder made you less likely to reveal a mental health issue yourself in your current workplace?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion32(questionNumber=None):
    # Have you had a mental health disorder in the past?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion33(questionNumber=None):
    # Do you currently have a mental health disorder?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion34(questionNumber=None):
    # Have you ever been diagnosed with a mental health disorder?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %questionNumber)
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %questionNumber) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion35(questionNumber=None):
    # If you have a mental health disorder, how often do you feel that it interferes with your work when being treated effectively?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion36(questionNumber=None):
    # If you have a mental health disorder, how often do you feel that it interferes with your work when not being treated effectively (i.e., when you are experiencing symptoms)?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion37(questionNumber=None):
    # What country do you work in?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion38(questionNumber=None):
    # What US state or territory do you work in?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion39(questionNumber=None):
    # If you have been diagnosed or treated for a mental health disorder, do you ever reveal this to clients or business contacts?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion40(questionNumber=None):
    # If you have been diagnosed or treated for a mental health disorder, do you ever reveal this to coworkers or employees?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion41(questionNumber=None):
    # Do you believe your productivity is ever affected by a mental health issue?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion42(questionNumber=None):
    # If yes, what percentage of your work time (time performing primary or secondary job functions) is affected by a mental health issue?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == '%', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion43(questionNumber=None):
    # Have you observed or experienced an unsupportive or badly handled response to a mental health issue in your current or previous workplace?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion44(questionNumber=None):
    # Would you feel more comfortable talking to your coworkers about your physical health or your mental health?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion45(questionNumber=None):
    # Have you ever discussed your mental health with your employer?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion46(questionNumber=None):
    # Describe the conversation you had with your employer about your mental health, including their reactions and what actions were taken to address your mental health issue/questions.
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()
    print("\nPERSONAL EXPERIENCES OF THE PEOPLE, CANNOT BE USED.")
    return

#Wordt meegenomen
def filterQuestion47(questionNumber=None):
    # Have you ever discussed your mental health with coworkers?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion48(questionNumber=None):
    # Describe the conversation with coworkers you had about your mental health including their reactions.
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = cursor.fetchall()
    for i in data:
        print(i)
    print("\nPERSONAL EXPERIENCES OF THE PEOPLE, CANNOT BE USED.")
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion49(questionNumber=None):
    # Have you ever had a coworker discuss their or another coworker's mental health with you?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion50(questionNumber=None):
    # Describe the conversation your coworker had with you about their mental health (please do not use names)
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()
    print("\nPERSONAL EXPERIENCES OF THE PEOPLE, CANNOT BE USED.")
    return

#Wordt meegenomen
def filterQuestion51(questionNumber=None):
    # Overall, how much importance does your employer place on physical health?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion52(questionNumber=None):
    # Overall, how much importance does your employer place on mental health?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion53(questionNumber=None):
    # If you have revealed a mental health disorder to a client or business contact, how has this affected you or the relationship?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion54(questionNumber=None):
    # If you have revealed a mental health disorder to a coworker or employee, how has this impacted you or the relationship?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion55(questionNumber=None):
    # Was your employer primarily a tech company/organization?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion56(questionNumber=None):
    # Would you have felt more comfortable talking to your previous employer about your physical health or your mental health?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion57(questionNumber=None):
    # Did you ever discuss your mental health with your previous employer?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion58(questionNumber=None):
    # Describe the conversation you had with your previous employer about your mental health, including their reactions and actions taken to address your mental health issue/questions.
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()
    print("\nPERSONAL EXPERIENCES OF THE PEOPLE, CANNOT BE USED.")
    return

#Wordt meegenomen
def filterQuestion59(questionNumber=None):
    # Did you ever discuss your mental health with a previous coworker(s)?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion60(questionNumber=None):
    # Describe the conversation you had with your previous coworkers about your mental health including their reactions.
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()
    print("\nPERSONAL EXPERIENCES OF THE PEOPLE, CANNOT BE USED.")
    return

#Wordt meegenomen
def filterQuestion61(questionNumber=None):
    # Did you ever have a previous coworker discuss their or another coworker's mental health with you?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion62(questionNumber=None):
    # Describe the conversation your coworker had with you about their mental health (please do not use names).
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()
    print("\nPERSONAL EXPERIENCES OF THE PEOPLE, CANNOT BE USED.")
    return

#Wordt meegenomen
def filterQuestion63(questionNumber=None):
    # Overall, how much importance did your previous employer place on physical health?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion64(questionNumber=None):
    # Overall, how much importance did your previous employer place on mental health?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion65(questionNumber=None):
    # Are you openly identified at work as a person with a mental health issue?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion66(questionNumber=None):
    # Has being identified as a person with a mental health issue affected your career?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion67(questionNumber=None):
    # How has it affected your career?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion68(questionNumber=None):
    # If they knew you suffered from a mental health disorder, how do you think that your team members/co-workers would react?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion69(questionNumber=None):
    # Describe the circumstances of the badly handled or unsupportive response.
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()
    print("\nPERSONAL EXPERIENCES OF THE PEOPLE, CANNOT BE USED.")
    return

#Wordt meegenomen
def filterQuestion70(questionNumber=None):
    # Have you observed or experienced supportive or well handled response to a mental health issue in your current or previous workplace?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Overgeslagen
def filterQuestion71(questionNumber=None):
    # Describe the circumstances of the supportive or well handled response.
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion72(questionNumber=None):
    # Overall, how well do you think the tech industry supports employees with mental health issues?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion73(questionNumber=None):
    # Briefly describe what you think the industry as a whole and/or employers could do to improve mental health support for employees.
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()
    print("\nPERSONAL EXPERIENCES OF THE PEOPLE, CANNOT BE USED.")
    return

#Overgeslagen
def filterQuestion74(questionNumber=None):
    # If there is anything else you would like to tell us that has not been covered by the survey questions, please use this space to do so.
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()
    print("\nPERSONAL EXPERIENCES OF THE PEOPLE, PROBABLY CANNOT BE USED.")
    return

#Wordt meegenomen
def filterQuestion75(questionNumber=None):
    # Would you be willing to talk to one of us more extensively about your experiences with mental health issues in the tech industry? (Note that all interview responses would be used _anonymously_ and only with your permission.)
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isdigit(s) or s == '.' or s == ',' or s == '-', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion76(questionNumber=None):
    # What is your race?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion77(questionNumber=None):
    # Do you think that discussing a physical health issue with your employer would have negative consequences?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion78(questionNumber=None):
    # Do you feel that your employer takes mental health as seriously as physical health?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion79(questionNumber=None):
    # If you have a mental health condition, do you feel that it interferes with your work?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion80(questionNumber=None):
    # Do you work remotely (outside of an office) at least 50% of the time?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion81(questionNumber=None):
    # Do you know the options for mental health care your employer provides?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion82(questionNumber=None):
    # Has your employer ever discussed mental health as part of an employee wellness program?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion83(questionNumber=None):
    # Does your employer provide resources to learn more about mental health issues and how to seek help?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion84(questionNumber=None):
    # How easy is it for you to take medical leave for a mental health condition?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion85(questionNumber=None):
    # Do you think that discussing a mental health issue with your employer would have negative consequences?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion86(questionNumber=None):
    # Would you be willing to discuss a mental health issue with your coworkers?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion87(questionNumber=None):
    # Would you be willing to discuss a mental health issue with your direct supervisor(s)?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion88(questionNumber=None):
    # Would you bring up a physical health issue with a potential employer in an interview?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion89(questionNumber=None):
    # Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Overgeslagen
def filterQuestion90(questionNumber=None):
    # Any additional notes or comments
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = cursor.fetchall()
    for i in data:
        print(i)
    connector.commit()
    print("\nPERSONAL EXPERIENCES OF THE PEOPLE, CANNOT BE USED.")
    return

#Wordt meegenomen
def filterQuestion91(questionNumber=None):
    # Do you think that discussing a mental health disorder with your employer would have negative consequences?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion92(questionNumber=None):
    # Have you heard of or observed negative consequences for co-workers who have been open about mental health issues in your workplace?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion93(questionNumber=None):
    # If you have revealed a mental health issue to a client or business contact, do you believe this has impacted you negatively?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion94(questionNumber=None):
    # If you have revealed a mental health issue to a coworker or employee, do you believe this has impacted you negatively?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion95(questionNumber=None):
    # Do you think that discussing a mental health disorder with previous employers would have negative consequences?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion96(questionNumber=None):
    # Do you think that discussing a physical health issue with previous employers would have negative consequences?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion97(questionNumber=None):
    # Would you have been willing to discuss a mental health issue with your previous co-workers?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion98(questionNumber=None):
    # Did you feel that your previous employers took mental health as seriously as physical health?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion99(questionNumber=None):
    # Did you hear of or observe negative consequences for co-workers with mental health issues in your previous workplaces?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion100(questionNumber=None):
    # Do you feel that being identified as a person with a mental health issue would hurt your career?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Wordt meegenomen
def filterQuestion101(questionNumber=None):
    # Do you think that team members/co-workers would view you more negatively if they knew you suffered from a mental health issue?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or str.isdigit(s) or s == '.' or s == ',' or s == '-' or s == ' ' or s == "'" or s == '/', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    print("\nDID NOT FILTER THE APOSTOPHES BECAUSE OF THE APOSTROPHES IN TEXT")
    return

#Overgeslagen
def filterQuestion102(questionNumber=None):
    # If yes, what condition(s) have you been diagnosed with?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    print(data)
    connector.commit()
    print("\nDID NOT FILTER THE BRACKETS BECAUSE OF THE BRACKETS IN TEXT")
    return

#Overgeslagen
def filterQuestion103(questionNumber=None):
    # If maybe, what condition(s) do you believe you have?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    print(data)
    connector.commit()
    print("\nDID NOT FILTER THE BRACKETS BECAUSE OF THE BRACKETS IN TEXT")
    return

#Overgeslagen
def filterQuestion104(questionNumber=None):
    # Which of the following best describes your work position?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

#Wordt meegenomen
def filterQuestion105(questionNumber=None):
    # Do you work remotely?
    cursor.execute("SELECT * FROM Question WHERE (questionid = %s)" %(questionNumber + 13))
    print("THE QUESTION IS:")
    print(str(cursor.fetchone())+"\n")
    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = '%s')" %(questionNumber + 13)) #SQL Statement
    data = list(cursor.fetchall())
    newData = str("".join(filter(lambda s: str.isalpha(s) or s == '.' or s == ',' or s == '-' or s == ' ', str(data))))
    print(newData.replace(",,", ", "))
    connector.commit()
    return

def generator():
    print("import sqlite3")
    print("database = " + "'mental_health.sqlite'")
    print("\nconnector = sqlite3.connect(database)")
    print("cursor = connector.cursor()\n")
    for x in range(105):
        print("def filterQuestion" + str(x+1) +"():")
        print('    cursor.execute("SELECT DISTINCT AnswerText FROM Answer WHERE (QuestionID = ' + '%s' + ')" %questionNumber)') #SQL Statement
        print("    data = cursor.fetchall()")
        print("    for i in data:")
        print("        print(i)")
        print("    connector.commit()")
        print("    return\n")

def main():
    print("Which question do you want to select?")
    number = input("Select Question number (1 to 105): ")
    if int(number) >= 1 and int(number) <= 105:
        print("Executing function: 'filterQuestion" + str(number) + "()'!\n\n\n")
        result = eval('filterQuestion'+ number +'(questionNumber='+ number +')')
    else:
        print("Bad input.")
    connector.close()
    # generator()

if __name__ == "__main__":
    main()