#6. Activity Logging

import datetime

def log_activity(user, action):
    with open("access.log", "a") as logfile:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logfile.write(f"[{time}] {user} -> {action}\n")

log_activity("admin", "Accessed Settings")
log_activity("guest", "Tried to Delete File")
print("File Created")
