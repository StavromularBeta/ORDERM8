import datetime
import os, sys, inspect
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import SQL_functions as sq

# matplotlib stuff

import matplotlib
import numpy as np
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


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


def generate_tasks_for_day():
    current_day = datetime.datetime.today().weekday()
    daydict = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    current_day = daydict[current_day]
    tasks = sq.search_by_day_of_week(current_day)
    taskdict = {}
    for item in tasks:
        taskdict[item[0]] = item[3]
    return taskdict.items()


def enter_customer_into_daily(customer_information):
    sq.new_daily_customer(customer_information)


def get_todays_current_customers():
    todays_customers = sq.return_all_daily_customer_entries()
    customer_list = []
    for item in todays_customers:
        customer_id = item[1]
        customer = sq.search_by_customer_id(customer_id)
        for otheritem in customer:
            name = otheritem[1] + " " + otheritem[2]
        customer_list.append(name)
    return customer_list


def create_weekly_customer_figure(tk_frame):
    f = Figure(figsize=(4,4), dpi=100)
    ax = f.add_subplot(111)
    wgd = sq.weekly_graph_data()
    x_labels = np.array(["M", "T", "W", "Th", "F"])
    y_axis = np.array([wgd[0], wgd[1], wgd[2], wgd[3], wgd[4]])
    w = 3
    nitems = len(y_axis)
    x_axis = np.arange(0, nitems*w, w)
    ax.bar(x_axis, y_axis, width=w, align='center',)
    ax.set_xticks(x_axis)
    ax.set_yticks(np.arange(0, nitems+1, 1))
    ax.set_xticklabels(x_labels)
    ax.set_ylabel('Deliveries')
    ax.set_xlabel('Weekday')
    ax.set_title("This Week's Deliveries")
    f.tight_layout()
    canvas = FigureCanvasTkAgg(f, tk_frame)
    canvas.show()
    return canvas





