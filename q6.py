# 6.	A company needs a program that reads employee names and their basic salary.
# The program should: Calculate total salary including HRA (20%) and DA (10%).
# Stop taking input when the user types "stop". Display each employee’s total salary at the end.
# Concepts: while loop, arithmetic operations, condition check, formatted output.
counter = 0
i = 0
emply_input_name = [0]*100
emply_input_salary = [0]*100
while (counter == 0):
    emply_input_name[i] = input("enter name: ")
    emply_input_salary[i] = int(input("enter salary: "))
    i = i + 1
    usr_input_con_break = input (" ")
    if usr_input_con_break == 'stop':
        counter = counter + 1

emply_total_sal = [0]*100

hra = 0.2
da = 0.1

i = 0
while i<100 and emply_input_salary[i] != 0:
    emply_total_sal[i] = emply_input_salary[i] + (emply_input_salary[i]*0.2) + (emply_input_salary[i]*0.1)
    i = i + 1

i = 0
while i<100 and emply_total_sal[i] != 0:
    print(f"{emply_input_name[i]}'s salary: {emply_total_sal[i]}")
    i = i + 1
