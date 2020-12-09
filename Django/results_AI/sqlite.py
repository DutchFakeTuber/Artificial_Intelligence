import sqlite3, csv, random, datetime, os

"""
This sqlite program is made for:
    Injecting dataset data into the table;
    Resetting the Survey table, making it blank again.
"""
csvfilepath = "dataset.csv"
database = "../db.sqlite3"

# Function for reading table 'results_AI_resultsdataset' and 'results_AI_resultssurvey'
print(os.getcwd())

def checkTable():
    connector = sqlite3.connect(database)
    cursor = connector.cursor()

    # Fetch data from the dataset table
    cursor.execute("SELECT * FROM results_AI_resultsdataset")
    # Fetch all rows from table
    data = cursor.fetchall()
    # Print one row at a time
    print("Data in the Dataset Table:\n")
    for x in data:
        print(x)

    # Fetch data from the survey table
    cursor.execute("SELECT * FROM results_AI_resultssurvey")
    # Fetch all rows from table
    data = cursor.fetchall()
    # Print one row at a time
    print("\nData in the Survey Table:\n")
    for x in data:
        print(x)

    connector.close()

def tableInjector(amount=25):
    connector = sqlite3.connect(database)
    cursor = connector.cursor()
    
    for y in range(amount):
        choice = [0.0, 0.5, 1.0]
        randomGen = [
        random.choice(choice), random.choice(choice), random.choice(choice),
        random.choice(choice), random.choice(choice), random.choice(choice),
        random.choice(choice), random.choice(choice), random.choice(choice),
        random.choice(choice), random.choice(choice), random.choice(choice)
    ]
        randomDict = {
            f"question_{i + 1}": x for i, x in zip(range(12), randomGen)
        }

        command = (
            "INSERT INTO results_AI_resultssurvey ( \
                question_1, question_2, question_3, question_4, \
                question_5, question_6, question_7, question_8, \
                question_9, question_10, question_11, question_12, dateAndTime \
                ) VALUES ( \
                    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? \
                    )"
        )
        values = (
            randomDict["question_1"],  randomDict["question_2"],  randomDict["question_3"],
            randomDict["question_4"],  randomDict["question_5"],  randomDict["question_6"],
            randomDict["question_7"],  randomDict["question_8"],  randomDict["question_9"],
            randomDict["question_10"], randomDict["question_11"], randomDict["question_12"],
            datetime.datetime.now()
        )
        cursor.execute(command, values)
        connector.commit()
        print(f"Injected {y + 1} lines into the database.")

    connector.close()

def resetSurveyTable():
    connector = sqlite3.connect(database)
    cursor = connector.cursor()

    # First delete table if it is in the database
    cursor.execute("DROP TABLE IF EXISTS results_AI_resultssurvey")
    connector.commit()

    # Create new database table with the same name
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS 'results_AI_resultssurvey'( \
            'id' integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
            'question_1' real NOT NULL, \
            'question_2' real NOT NULL, \
            'question_3' real NOT NULL, \
            'question_4' real NOT NULL, \
            'question_5' real NOT NULL, \
            'question_6' real NOT NULL, \
            'question_7' real NOT NULL, \
            'question_8' real NOT NULL, \
            'question_9' real NOT NULL, \
            'question_10' real NOT NULL, \
            'question_11' real NOT NULL, \
            'question_12' real NOT NULL, \
            'dateAndTime' datetime NOT NULL \
            )"
    )
    connector.commit()

    cursor.execute("SELECT * FROM results_AI_resultssurvey")
    print(cursor.fetchone())

    connector.close()


def fillDatatasetTable():
    data = []
    # Read data from csv file
    with open(csvfilepath, 'r') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
        # Code for replacing the '' with None
        for row in reader:
            for i, x in enumerate(row[:]):
                if len(x) < 1:
                    x = row[i] = None
            # Put results as an array into data
            data.append(row)
        print(data)  # For testing only

    # Assign new arrays for each question
    question1 = []
    question2 = []
    question3 = []
    question4 = []
    question5 = []
    question6 = []
    question7 = []
    question8 = []
    question9 = []
    question10 = []
    question11 = []
    question12 = []
    # Skip first line in array
    iterdata = iter(data)
    next(iterdata)
    # For loop for filling the new arrays with data
    for x in iterdata:
        question1.append(x[1])
        question2.append(x[2])
        question3.append(x[3])
        question4.append(x[4])
        question5.append(x[5])
        question6.append(x[6])
        question7.append(x[7])
        question8.append(x[8])
        question9.append(x[9])
        question10.append(x[10])
        question11.append(x[11])
        question12.append(x[12])

    # Access Django database
    connector = sqlite3.connect(database)
    cursor = connector.cursor()
    # Injecting data into the database table 'results_AI_resultsdataset' one line at a time.
    # Change if statement
    for a, b, c, d, e, f, g, h, i, j, k, l in zip(question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12):
        command = " \
            INSERT INTO results_AI_resultsdataset \
            (question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10, question_11, question_12) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        values = (a, b, c, d, e, f, g, h, i, j, k, l)
        cursor.execute(command, values)
        connector.commit()

    # Read table 'results_AI_resultsdataset'
    cursor.execute("SELECT * FROM results_AI_resultsdataset")
    # Fetch all lines
    data = cursor.fetchall()
    # Print one line at a time
    for x in data:
        print(x)

    # Closing connection with database
    connector.close()


def main():
    # resetSurveyTable()
    # fillDatatasetTable()
    # checkTable()
    tableInjector() # Add keyword argument (**kwargs) amount={number} if you want more or less lines added than 25.


if __name__ == "__main__":
    main()

