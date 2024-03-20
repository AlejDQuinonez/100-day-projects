import time 
import datetime
import bisect

start_time = time.time()
lap_number = 1
user_choice = ""

def binary_search(the_list, element):
    i = bisect.bisect_left(the_list, element)

    if i != len(the_list) and the_list[i] == element:
        return i
    else:
        return -1

def countdown(hour, minute, second):
    total_seconds = hour * 3600 + minute * 60 + second

    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)

        print(timer, end = "\r")

        time.sleep(1)
        total_seconds -= 1
    
    print("DONE, The countdown is at zero seconds!")

def lap_timer(value ,lap):
    while value.lower() != "q":
        value = input()

        
        last_time = start_time
        

        lap_time   = round((time.time() - last_time), 2)
        total_time = round((time.time() - start_time), 2)

        print("Lap No. "     + str(lap))
        print("Total Time: " + str(total_time))
        print("Lap Time: "   + str(lap_time))

        print("*" * 20)

        last_time = time.time()
        lap += 1

    print("Done")


while user_choice != "4":
    print("Welcome to the program timers, were limited to 3 timers at the moment.")
    print("please choose one")
    print("1. Random number search task for computer")
    print("2. Countdown timer")
    print("3. Stopwatch")
    print("4. EXIT")

    user_choice = input()

    if user_choice == "2":
        hour   = input("Enter the time in hours: ")
        minute = input("Enter the time in minute: ")
        second = input("Enter the time in second: ")
        
        countdown(int(hour), int(minute), int(second))

    elif user_choice == "3":
        print("Press ENTER for each lap. \nAnd Type Q with ENTER to stop the timer.")
        
        lap_timer(user_choice, lap_number)

    elif user_choice == "1":
        our_list = list(range(10000000))
        element  = 7000000

        start = time.time()
        
        binary_search(our_list, element)

        end = time.time()

        print(f"It took the computer {end - start} seconds to find the element using binary search.")

print("Good-Bye.")