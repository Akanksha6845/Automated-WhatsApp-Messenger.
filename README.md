# WhatsApp Message Scheduler

This project allows you to schedule WhatsApp messages to be sent at a specified date and time using Python and the `pywhatkit` library.

## Features

- **Send WhatsApp messages automatically**: Schedule a message to be sent at a specific date and time.
- **Supports any recipient number**: Input the recipient’s phone number along with the country code.
- **Input validation**: Checks if the scheduled time is in the future and alerts if not.

## Requirements

- Python 3.x
- `pywhatkit` library
- `datetime` module (part of Python’s standard library)

## Installation

To use this project, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/whatsapp-message-scheduler.git
    cd whatsapp-message-scheduler
    ```

2. Install the required dependencies:

    ```bash
    pip install pywhatkit
    ```

3. Make sure you have a working version of WhatsApp Web open in your default browser.

## Usage

1. Run the script:

    ```bash
    python schedule_message.py
    ```

2. When prompted, enter the following:

    - **Recipient's phone number**: The phone number of the person you want to message, including the country code (e.g., +919123456789).
    - **Message to send**: The message you wish to send.
    - **Date**: The date (YYYY-MM-DD) you want the message to be sent.
    - **Time**: The time (HH:MM in 24-hour format) at which you want the message to be sent.

3. The script will automatically open WhatsApp Web at the specified time and send the message to the recipient.

## Example

```bash
Enter recipient number (with country code, e.g., +919123456789): +919876543210
Enter the message to send: Hello! This is a scheduled message.
Enter the date (YYYY-MM-DD): 2025-04-20
Enter time (HH:MM in 24-hr format): 14:30
