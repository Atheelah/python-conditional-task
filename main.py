# speed per locations
# speed more than speed limit
# give 1 demerit point per 5km (over)


speed = int(input("Please Enter Speed :"))
speed_limit = int(input("Please Enter Speed Limit :"))
if speed <= speed_limit:
    print("OK")
elif speed > speed_limit:
    demerits = (speed-speed_limit)/5
    print("points :", demerits)
    if demerits >12:
        print("Time to go to Jail")
