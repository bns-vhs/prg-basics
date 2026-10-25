car_speed = int(input('what was your speed?:'))
speed_limit_min = 40
speed_limit_max = 140
if car_speed in range(speed_limit_min, speed_limit_max + 1):
    print("You are safe")
else:
    print("You are not safe")