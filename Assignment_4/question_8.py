# 8. Write a python script to calculate simple interest.
pa=int(input("Enter Principle Amount:"))
roi=int(input("Enter Rate Of Interest:"))
t=int(input("Enter the time period in year:"))
si=(pa*roi*t)/100
print("Simple interest is",si)