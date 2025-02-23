import schedule
import time

def my_task(func):
    print("Running scheduled task...")

    # Schedule the task (Example: Run every minute)
    schedule.every(1).minutes.do(func)

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(1)
