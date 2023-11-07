# %%

import tkinter as tk
import psycopg2
import requests

# My openweatherAPI key
api_key = "c428054aad96b8eeb18e241730d8cb9d"

# connection to my local postgreSQL server
conn = psycopg2.connect(
    host="127.0.0.1",
    database="stationzuil",
    user="postgres",
    password="Tijnijburg12",
    port=5432
)
cursor = conn.cursor()

# Function to get the most recent 5 messages and authors from the database
def fetch_recent_messages_with_authors():
    cursor.execute("SELECT message, author FROM comments ORDER BY datetime DESC LIMIT 5")
    messages_with_authors = cursor.fetchall()
    return messages_with_authors

# this function grabs the weather from the api key and displayes the temperature in celcius after converting it from kelvin
def display_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        celcius = temperature - 273.15
        celcius = round(celcius)
        message_listbox.insert(tk.END, f"Temperature in {city}: {celcius}°C")
    else:
        message_listbox.insert(tk.END, "Temperature data not available")

# here i made the tkinter window
root = tk.Tk()
root.title("NS berichten en weer!")

# Create and configure the window
message_text = tk.StringVar()

message_label = tk.Label(root, text="Most Recent Messages with Authors and Weather:")
message_label.pack()

# here i increase the window size
message_listbox = tk.Listbox(root, width=100, height=15, selectmode=tk.SINGLE)  # Increased width and height
message_listbox.pack()

# here we put all the messages and authors in
def populate_listbox():
    messages_with_authors = fetch_recent_messages_with_authors()
    for message, author in messages_with_authors:
        entry = f"Author: {author} | Message: {message}"
        message_listbox.insert(tk.END, entry)

populate_listbox()

# we grab the weather from a certain city in this case amsterdam 
def get_weather():
    city = "Amsterdam"  # Replace with the desired city
    display_weather(city)

weather_button = tk.Button(root, text="Weer in amsterdam", command=get_weather)
weather_button.pack()

root.mainloop()

# %%
