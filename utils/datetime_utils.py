import datetime
import time
def show_current_datetime():
    now=datetime.datetime.now()
    print("Current Date and Time :", now.strftime("%Y-%m-%d %H-%M-%S"))
def date_difference():
    d1=input("Enter first date (YYYY-MM-DD) : ")
    d2=input("Enter second date (YYYY-MM-DD) : ")
    date1=datetime.datetime.strptime(d1, "%Y-%m-%d")
    date2=datetime.datetime.strptime(d2, "%Y-%m-%d")
    diff=abs((date2-date1).days)
    print("Difference :", diff,"days")
def format_date():
    now=datetime.datetime.now()
    print("Formatted Date (DD/MM/YYYY) :", now.strftime("%d/%m/%Y"))
def stopwatch():
    input("Press Enter to START stopwatch ....")
    start=time.time()
    input("Press Enter to Stop ....")
    end=time.time()
    print("Elapsed Time :", round(end-start, 2), "seconds")
def countdown():
    sec=int(input("Enter seconds : "))
    for i in range(sec, 0, -1):
        print(i)
        time.sleep(1)
    print("Time's up!")
