""" 5. Create four variables in a Python script and assign values of different data types to them. Write a Python script to print value, its type and id of each variable"""

name="krishna"
age=20
fee=3600.52
age_check=20>22

# value of variable.
print("value of variable:")
print(name,age,fee,age_check,sep="\n",end="\n\n")

# id of variable.
print("Id of variable:")
print(id(name),id(age),id(fee),id(age_check),sep="\n",end="\n\n")

# type of Variable
print("type of variable:")
print(type(name),type(age),type(fee),type(age_check),sep="\n")