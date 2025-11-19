#traffic system records speed of vehicals every 12 hours
#program reads 12 speed values. calculate the avg speed.
#if avg speed less than 40 -> slow
#if avg speed 40 to 80 -> moderate
#if avg > 80 -> fast
speedList = [0]*12
for i in range (0, 12, 1):
    speedList[i] = float(input("enter speed ="))

total = 0

for i in range (0,12,1):
    total = total + speedList[i]

avg = total/12

if avg>40.0:
    print("slow traffic")
elif avg>=40.0 and avg<80.0:
    print("moderate traffic")
elif avg>80.0:
    print("high traffic")
