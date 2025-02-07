import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    charset="utf8",
    password="12345", 
    port = 3307
)
mycursor = ""

def submit():
    global mycursor
    # Creating Default database

    a = '''
    CREATE DATABASE IF NOT EXISTS chatbot;
    use chatbot;
    CREATE TABLE replies(reply varchar(200), repID int NOT NULL Primary Key);
    CREATE TABLE questions(que varchar(200), queID int NOT NULL);
    CREATE TABLE suggestions(sugID char(5) NOT NULL Primary Key, suggestion varchar(200), suggestion2 varchar(200), suggestion3 varchar(200), suggestion4 varchar(200),repID int, queID int, Foreign Key(repID) References replies(repID));
    INSERT INTO questions (que, queID)
    VALUES ("hi", 1);
    INSERT INTO questions (que, queID)
    VALUES ("hello", 2);
    INSERT INTO questions (que, queID)
    VALUES ("what are you", 4);
    INSERT INTO questions (que, queID)
    VALUES ("what can you do", 5);
    INSERT INTO questions (que, queID)
    VALUES ("who are you", 4);
    INSERT INTO questions (que, queID)
    VALUES ("youtube", 3);
    INSERT INTO questions (que, queID)
    VALUES ("open chrome", 3);
    INSERT INTO questions (que, queID)
    VALUES ("open spotify", 3);
    INSERT INTO questions (que, queID)
    VALUES ("reminder", 9);
    INSERT INTO questions (que, queID)
    VALUES ("suggest", 3);
    INSERT INTO replies (reply, repID)
    VALUES ("How may i help you?", 1);
    INSERT INTO replies (reply, repID)
    VALUES ("Please guide me in what case i can assist you with?", 2);
    INSERT INTO replies (reply, repID)
    VALUES ("Sure!", 3);
    INSERT INTO replies (reply, repID)
    VALUES ("I am an application powered with AI created by Divyam Mathur.", 4);
    INSERT INTO replies (reply, repID)
    VALUES ("Thrilled that you asked!, see the suggestions area", 5);
    INSERT INTO replies (reply, repID)
    VALUES ("Sorry but for the time being, I am not equipped to do that.", 6);
    INSERT INTO replies (reply, repID)
    VALUES ("See below", 7);
    INSERT INTO replies (reply, repID)
    VALUES ("Just a sec..", 8);
    INSERT INTO replies (reply, repID)
    VALUES ("Sure! You will be reminded after 5 minutes.", 9);
    INSERT INTO suggestions(sugID, suggestion, suggestion2, suggestion3, repID)
    VALUES ("a", "open youtube", "open chrome", "open spotify", 1);
    INSERT INTO suggestions(sugID, suggestion, suggestion2, suggestion3, repID)
    VALUES ("b", "open youtube", "open chrome", "open spotify", 2);
    INSERT INTO suggestions (sugID, suggestion repID)
    VALUES ("d", "about me", 5);
    INSERT INTO suggestions(sugID, suggestion, suggestion2, suggestion3, repID)
    VALUES ("e", "open youtube", "open chrome", "open spotify", 4);
    INSERT INTO suggestions (sugID, suggestion, suggestion2, suggestion3, suggestion4 repID)
    VALUES ("f", "open any application", "Speaking in English", "Tell Jokes", "Weather Forecasting" 8);
    '''
    mycursor = mydb.cursor()
    a = a.replace("\n", " ")
    a = a.replace("\"", "'")
    lines = a.split(";")
    for line in lines:
        newLine = line.replace(" ", "")
        if not newLine:
            continue
        line = line + ";"
        # print(line)
        try:
            mycursor.execute(line)
        except:
            pass


if __name__ == "__main__":
    submit()