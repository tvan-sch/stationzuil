#%%
import random
import datetime
import csv

def main():
    # here we make the list of the potential 3 stations
    stations = ['Amsterdam Centraal', 'Utrecht Centraal', 'Rotterdam Centraal']

    filename = "zuil.csv"

    # here we ask for the users name if the string is emtpy it will be Anonymous
    name = input("Enter your name (or leave it empty for anonymity): ")
    if not name:
        name = "anoniem"

    # here we ask the user for the input by using the len function combined with an if statement we can make sure its not over 140 characters
    message = input("Wat is je bericht (140 karakters max): ")
    if len(message) > 140:
        print("Je bericht is te lang!")
        return

    # here we use our datetime library to get the current time to put in our final document
    current_time = datetime.datetime.now()

    # here we use our current time and make sure its in iso standard format
    formatted_time = current_time.isoformat()

    # this is just an easy way to get the random station at wich it will be displayed
    station = random.choice(stations)
    
    # here we open our file and write our previous variable
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([message, formatted_time, name, station])

    print(f"Message saved to {filename}")

main()
# %%
