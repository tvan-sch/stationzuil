# %%
import csv
import psycopg2
import datetime

def main():
    # Database connection
    connection = psycopg2.connect(
        host="127.0.0.1",
        database="stationzuil",
        user="postgres",
        password="Tijnijburg12",
        port=5432
    )

    # asks for input then checks if it is empty 
    name = input("What is your name? ")
    if not name:
        print("Input can not be left empty")
        return

    # same thing 
    email = input("What is your Email-adress? ")
    if not email:
        print("Input can not be left empty")
        return

    # we open our csv file and add a newline 
    with open("zuil.csv", newline="") as f:
        reader = csv.reader(f)
        # we read all the rows asign them new values
        for row in reader:
            process_row(connection, name, email, row)
    
    print("All messages processed.")

    # this empties the file after usage
    with open("zuil.csv", "w") as f:
        pass
    print("CSV file cleared.")


#function that ultimatly will edit our csv file
def process_row(connection, moderator_name, moderator_email, row):
    message, formatted_time, name, station = row
    date = datetime.datetime.fromisoformat(formatted_time)

    #this prints what the moderator will see after wich he can make a choice at wich it wil be printed or not
    print(f"New message, Station: {station}, Author: {name}, Message: {message}")

    # if you type n it will be rejected anything else will make it accepted
    acceptedResponse = input("Do you want to accept the previous message? (Y/n) ")
    accepted = False if acceptedResponse == "n" else True

    # we grab the current time of moderation 
    review_time = datetime.datetime.now()

    cur = connection.cursor()
    # we insert all the data into our postgressql serverr in this order 
    cur.execute("INSERT INTO comments (datetime, author, message, station, accepted, rating_date, moderator_name, moderator_email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (
            date,
            name,
            message,
            station,
            accepted,
            review_time,
            moderator_name,
            moderator_email
        )
    )
    # it commits so that the changes are final and prints that it was succesfull
    connection.commit()
    print("Message inserted into the database.")








main()


