WhatsApp Message Scheduler
This project allows you to schedule WhatsApp messages to be sent at a specified date and time using Python and the pywhatkit library.

Features
Send WhatsApp messages automatically: Schedule a message to be sent at a specific date and time.

Supports any recipient number: Input the recipient’s phone number along with the country code.

Input validation: Checks if the scheduled time is in the future and alerts if not.

Requirements
Python 3.x

pywhatkit library

datetime module (part of Python’s standard library)

Installation
To use this project, follow these steps:

Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/your-username/whatsapp-message-scheduler.git
cd whatsapp-message-scheduler
Install the required dependencies:

bash
Copy
Edit
pip install pywhatkit
Make sure you have a working version of WhatsApp Web open in your default browser.

Usage
Run the script:

bash
Copy
Edit
python schedule_message.py
When prompted, enter the following:

Recipient's phone number: The phone number of the person you want to message, including the country code (e.g., +919123456789).

Message to send: The message you wish to send.

Date: The date (YYYY-MM-DD) you want the message to be sent.

Time: The time (HH:MM in 24-hour format) at which you want the message to be sent.

The script will automatically open WhatsApp Web at the specified time and send the message to the recipient.

Example
bash
Copy
Edit
Enter recipient number (with country code, e.g., +919123456789): +919876543210
Enter the message to send: Hello! This is a scheduled message.
Enter the date (YYYY-MM-DD): 2025-04-20
Enter time (HH:MM in 24-hr format): 14:30
License
This project is licensed under the MIT License - see the LICENSE file for details.
