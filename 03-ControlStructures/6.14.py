facebook = bool(int(input("Do you have facebook? 1/0 ")))
twitter = bool(int(input("Do you have twitter? 1/0 ")))
instagram = bool(int(input("Do you have instagram? 1/0 ")))
goodness=0
if facebook == True:
    goodness+= 1
if twitter == True:
    goodness+= 1
if instagram== True:
    goodness+= 1

if goodness>=2:
    print("You are a good influencer")
else:
    print("bad")