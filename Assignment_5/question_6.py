# 6. Write a python script which takes a three digit number from the user and displays only its middle digit.
num=int(input("Enter three digit number:"))
q=num//10
m=q%10
print("Middile digit of entered number is",m)
