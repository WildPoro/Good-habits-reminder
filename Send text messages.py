"""Author
Kristian Zotka  
[LinkedIn](https://www.linkedin.com/in/kristian-zotka)"""

from twilio.rest import Client
import psycopg2
import schedule
import time

sid = '################################' # Get info from you twilio dashboard
token = '############################' # Get info from you twilio dashboard
twilio_number = '################' # Get info from you twilio dashboard

DB_CONFIG = {
    "host": "#####",
    "database": "####",
    "user": "#####",
    "password": "####",
    "port": "#####"
}

def habits():
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()
    cursor.execute("SELECT habit FROM habits ORDER BY id limit 5")
    habits = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return habits

def subscribers():
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()
    cursor.execute("SELECT phone_number FROM subscribers")
    subscribers = [row[0] for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return subscribers

def send_message(number, message):
    try:
        client = Client(sid, token)
        client.messages.create(to=number, from_=twilio_number, body=message)
        print("Message sent")
    except Exception as e:
        print("Error: ", e)

def newsletter():
    habit_list = habits()
    subscriber_list = subscribers()
    message_body = "Hello this is Kristian's project! Here are your habits for today: \n"
    for habit in habit_list:
        message_body += habit + "\n"
    for number in subscriber_list:
        send_message(number, message_body)
    
schedule.every().day.at("23:36").do(newsletter)
   
while True:
    schedule.run_pending()
    time.sleep(60)
