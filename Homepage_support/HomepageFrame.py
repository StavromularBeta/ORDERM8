import datetime


def generate_current_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%A") + ", " + current_time.strftime("%B") + " " + \
                     current_time.strftime("%d") + ", " + current_time.strftime("%I") + ":" + \
                     current_time.strftime("%M") + " " + current_time.strftime("%p")
    return formatted_time


def generate_time_until_cutoff():
    current_time = datetime.datetime.now()
    cut_off_time = current_time.replace(hour=13, minute=0, second=0)
    time_to_cutoff = cut_off_time - current_time
    if time_to_cutoff.total_seconds() <= 0:
        cutoff_sentence = "(Past cut-off)"
        return cutoff_sentence
    else:
        hour_until_cutoff = int(time_to_cutoff.total_seconds()) / 3600
        if hour_until_cutoff >= 1:
            minutes_until_cutoff = int((float(time_to_cutoff.total_seconds() / 3600) - float(hour_until_cutoff))*60)
            cutoff_sentence = "(" + str(hour_until_cutoff) + "h " + str(minutes_until_cutoff) + \
                "m to cut-off)"
            return cutoff_sentence
        else:
            minutes_until_cutoff = time_to_cutoff.total_seconds() / 60
            cutoff_sentence = "(" + str(int(minutes_until_cutoff)) + "m to cut-off)"
            return cutoff_sentence



