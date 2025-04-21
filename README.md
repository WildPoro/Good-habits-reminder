# Good Habits Reminder

A multi-part Python project that automates the collection, storage, and delivery of daily habit reminders via SMS. This tool is designed to help users build better routines through automation and consistency.

 Project Overview

The project is broken down into three parts:

 Part 1: Habit Extraction
- Scrapes a list of recommended good habits from a specified website.
- Parses and filters relevant habit suggestions.

 Part 2: Data Storage
- Stores extracted habits in a local SQLite database.
- Ensures data persistence and easy access for future operations.

 Part 3: SMS Reminders
- Sends daily habit reminders to the user’s phone.
- Uses a Twilio virtual phone number to automate and schedule text messages.

## Technologies Used
- Python
- PostgreSQL
- Twilio API
- Requests / BeautifulSoup (for web scraping)


## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/WildPoro/good-habits-tracker.git
   cd good-habits-tracker
