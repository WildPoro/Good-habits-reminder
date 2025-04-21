"""Author
Kristian Zotka  
[LinkedIn](https://www.linkedin.com/in/kristian-zotka)"""

from habits_scraper import scrape
import psycopg2

conn = psycopg2.connect(
    host="######",
    database="######",
    user="######",  
    password="#####",
    port="#####"
)

def insert_data(habits):
    """Inserts scraped habits into PostgreSQL database."""
    try:
        cur = conn.cursor()

        for habit in habits:
            print(f" Inserting habit: {habit}") 
            cur.execute("INSERT INTO habits (habit, source) VALUES (%s, %s)", (habit, "Camille Styles"))

        conn.commit()
        print(" Habits successfully inserted!")

    except Exception as error:
        print(f" Database error: {error}")

    finally:
        cur.close()

if __name__ == "__main__":
    habits = scrape()  
    print(f" Scraped habits: {habits}")  
    insert_data(habits)  
    conn.close()
