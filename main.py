import pywhatkit
from datetime import datetime

# Get input
recipient_number = input("Enter recipient number (with country code, e.g., +919123456789): ")
message_body = input("Enter the message to send: ")
send_date = input("Enter the date (YYYY-MM-DD): ")
send_time = input("Enter time (HH:MM in 24-hr format): ")

# Parse datetime
try:
    dt = datetime.strptime(f"{send_date} {send_time}", "%Y-%m-%d %H:%M")
    now = datetime.now()

    if dt <= now:
        print("❌ Scheduled time is in the past. Please choose a future time.")
    else:
        # pywhatkit will automatically wait until the time
        pywhatkit.sendwhatmsg(
            phone_no=recipient_number,
            message=message_body,
            time_hour=dt.hour,
            time_min=dt.minute,
            wait_time=10  # time in seconds to wait before sending the message after opening browser
        )
        print(f"✅ Message scheduled for {dt.strftime('%Y-%m-%d %H:%M')}")
except Exception as e:
    print(f"❌ Error: {e}")
