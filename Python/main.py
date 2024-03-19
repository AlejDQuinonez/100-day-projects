import time 

start_time = time.time()
last_time = start_time
lap_number = 1
value = ""

print("Press ENTER for each lap. \n Type Q and press ENTER to stop.")

while value.lower() != "q":
    value = input()

    lap_time = round((time.time() - last_time), 2)

    total_time = round((time.time() - start_time), 2)

    print("Lap No. " + str(lap_number))
    print("Total Time: " + str(total_time))
    print("Lap Time: " + str(lap_time))

    print("*" * 20)

    last_time = time.time()
    lap_number += 1

print("Done")