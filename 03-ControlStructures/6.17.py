###
# Converts time from 24-hour format (hh:mm) to 12-hour format (h:mm am/pm)
#

time_24 = input("Enter time (24-hour format): ").strip()

hours = int(time_24[0:2])
minutes = time_24[3:5]

if hours >= 12:
    period = "pm"
else:
    period = "am"

if hours == 0:
    hours_12 = 12
elif hours > 12:
    hours_12 = hours - 12
else:
    hours_12 = hours

print(f"Time in 12-hour format: {hours_12}:{minutes}{period}")