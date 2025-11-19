#create a python program that asks the userhow far do they wantto travel
#if 3 or less than 3 miles then suggest bicycle
#if more than 3 but less than 300 miles suggest motorcycle
#if 300 miles or more suggest super car

usrMiles = int(input("how many miles do you want to travel?: \n"))

if (usrMiles <= 3):
    print("Ride a bicycle")
elif (usrMiles > 3 and usrMiles) < 300:
    print("Ride a motorbicycle")
else:
    print("use a super car")



