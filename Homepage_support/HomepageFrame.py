import datetime

def generate_current_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%A") + ", " + current_time.strftime("%B") + " " + \
                     current_time.strftime("%d") + ", " + current_time.strftime("%I") + ":" + \
                     current_time.strftime("%M") + " " + current_time.strftime("%p")
    return formatted_time
