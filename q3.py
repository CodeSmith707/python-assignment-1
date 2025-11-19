#user building a small program for a school. the user must enter students name and marks for 3 subjects. 
#the program should calculate total, avg and display a grade. if marks are not btwn 0 and100 show error

sub1 = int(input("subject 1 marks = "))
if (sub1<0 or sub1>100):
    print("error invalid entry")
    exit()
    
sub2 = int(input("subject 2 marks = "))
if (sub2<0 or sub2>100):
    print("error invalid entry")
    exit()
    
sub3 = int(input("subject 3 marks = "))
if (sub3<0 or sub3>100):
    print("error invalid entry")
    exit()

total = sub1+sub2+sub3
print("total = ", total)
avg = total / 3
print("avg =", avg)

if (avg >= 90):
    print("grade A is awarded")
elif (avg>=80 and avg<90):
    print("grade B is awarded")
elif (avg>=70 and avg<80):
    print("grade C is awarded")
elif (avg>=60 and avg<70):
    print("grade D is awarded")
elif (avg>=50 and avg<60):
    print("grade F is awarded")  
